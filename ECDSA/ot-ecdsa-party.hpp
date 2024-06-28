/*
 * fake-spdz-ecdsa-party.cpp
 *
 */

#include "Networking/Server.h"
#include "Networking/CryptoPlayer.h"
#include "Math/gfp.h"
#include "ECDSA/P256Element.h"
#include "Protocols/SemiShare.h"
#include "Processor/BaseMachine.h"

#include "ECDSA/preprocessing.hpp"
#include "ECDSA/sign.hpp"
#include "Protocols/Beaver.hpp"
#include "Protocols/fake-stuff.hpp"
#include "Protocols/MascotPrep.hpp"
#include "Processor/Processor.hpp"
#include "Processor/Data_Files.hpp"
#include "Processor/Input.hpp"
#include "GC/TinyPrep.hpp"
#include "GC/VectorProtocol.hpp"
#include "GC/CcdPrep.hpp"

#include <assert.h>

template<template<class U> class T>
void run(int argc, const char** argv)
{
    ez::ezOptionParser opt;
    EcdsaOptions opts(opt, argc, argv);
    opt.add(
            "", // Default.
            0, // Required?
            0, // Number of args expected.
            0, // Delimiter if expecting multiple args.
            "Use SimpleOT instead of OT extension", // Help description.
            "-S", // Flag token.
            "--simple-ot" // Flag token.
    );
    opt.add(
            "", // Default.
            0, // Required?
            0, // Number of args expected.
            0, // Delimiter if expecting multiple args.
            "Don't check correlation in OT extension (only relevant with MASCOT)", // Help description.
            "-U", // Flag token.
            "--unchecked-correlation" // Flag token.
    );
    opt.add(
            "", // Default.
            0, // Required?
            0, // Number of args expected.
            0, // Delimiter if expecting multiple args.
            "Fewer rounds for authentication (only relevant with MASCOT)", // Help description.
            "-A", // Flag token.
            "--auth-fewer-rounds" // Flag token.
    );
    opt.add(
            "", // Default.
            0, // Required?
            0, // Number of args expected.
            0, // Delimiter if expecting multiple args.
            "Use Fiat-Shamir for amplification (only relevant with MASCOT)", // Help description.
            "-H", // Flag token.
            "--fiat-shamir" // Flag token.
    );
    opt.add(
            "", // Default.
            0, // Required?
            0, // Number of args expected.
            0, // Delimiter if expecting multiple args.
            "Skip sacrifice (only relevant with MASCOT)", // Help description.
            "-E", // Flag token.
            "--embrace-life" // Flag token.
    );
    opt.add(
            "", // Default.
            0, // Required?
            0, // Number of args expected.
            0, // Delimiter if expecting multiple args.
            "No MACs (only relevant with MASCOT; implies skipping MAC checks)", // Help description.
            "-M", // Flag token.
            "--no-macs" // Flag token.
    );

    Names N(opt, argc, argv, 2);
    int n_tuples = 1000;
    if (not opt.lastArgs.empty())
        n_tuples = atoi(opt.lastArgs[0]->c_str());
    PlainPlayer P(N, "ecdsa");
    P256Element::init();
    P256Element::Scalar::next::init_field(P256Element::Scalar::pr(), false);

    P256Element::Scalar keyp;
    SeededPRNG G;
    keyp.randomize(G);

    typedef T<P256Element::Scalar> pShare;
    DataPositions usage;

// set up MAC_Checks for both curve points and scalars
    pShare::MAC_Check::setup(P);
    T<P256Element>::MAC_Check::setup(P);

    OnlineOptions::singleton.batch_size = 1;
    typename pShare::Direct_MC MCp(keyp);
    ArithmeticProcessor _({}, 0);
    typename pShare::TriplePrep sk_prep(0, usage);
    SubProcessor<pShare> sk_proc(_, MCp, sk_prep, P);
    pShare sk, __;
    // synchronize
    Bundle<octetStream> bundle(P);
    P.unchecked_broadcast(bundle);
    Timer timer;
    timer.start();
    auto stats = P.total_comm();
    sk_prep.get_two(DATA_INVERSE, sk, __);
    cout << "Secret key generation took " << timer.elapsed() * 1e3 << " ms" << endl;
    (P.total_comm() - stats).print(true);

    OnlineOptions::singleton.batch_size = (1 + pShare::Protocol::uses_triples) * n_tuples;
    typename pShare::TriplePrep prep(0, usage);
    prep.params.correlation_check &= not opt.isSet("-U");
    prep.params.fewer_rounds = opt.isSet("-A");
    prep.params.fiat_shamir = opt.isSet("-H");
    prep.params.check = not opt.isSet("-E");
    prep.params.generateMACs = not opt.isSet("-M");
    opts.check_beaver_open &= prep.params.generateMACs;
    opts.check_open &= prep.params.generateMACs;
    SubProcessor<pShare> proc(_, MCp, prep, P);
    typename pShare::prep_type::Direct_MC MCpp(keyp);
    prep.triple_generator->MC = &MCpp;

    bool prep_mul = not opt.isSet("-D");
    prep.params.use_extension = not opt.isSet("-S");
    vector<EcTuple<T>> tuples;
    preprocessing(tuples, n_tuples, sk, proc, opts);
    //check(tuples, sk, keyp, P);
    sign_benchmark(tuples, sk, MCp, P, opts, prep_mul ? 0 : &proc);

    pShare::MAC_Check::teardown();
    T<P256Element>::MAC_Check::teardown();
    P256Element::finish();
}

void calculate_key_sum(int argc, const char** argv) {
    // Initialize command-line options
    ez::ezOptionParser opt;
    opt.add("", 1, 1, 0, "Player number (0 or 1)", "-p", "--player");
    opt.add("", 1, 1, 0, "Hostname of the server", "-h", "--hostname");
    opt.parse(argc, argv);

    int player_num;
    std::string hostname;
    opt.get("-p")->getInt(player_num);
    opt.get("-h")->getString(hostname);

    // Initialize networking
    int port_base = 5001;  // Default base port number
    Names N(player_num, 2, hostname, port_base);
    PlainPlayer player(N, "calculate_key_sum");

    // Initialize curve parameters
    P256Element::init();
    P256Element::Scalar::next::init_field(P256Element::Scalar::pr(), false);

    // Timing key generation
    Timer key_timer;
    key_timer.start();

    // Generate the secret key for each player
    SeededPRNG G;
    P256Element::Scalar alphai;
    alphai.randomize(G);

    // Generate the public key for this player
    P256Element alphaiG(alphai);

    key_timer.stop();
    std::cout << "Client public key share generation time: " << key_timer.elapsed() * 1e3 << " ms" << std::endl;

    // Pack the public key into an octetStream
    octetStream os;
    alphaiG.pack(os);

    // Initialize variables
    P256Element betaG, product;

    if (player_num == 0) {
        // P_1 (Player 0) will receive P_2's public key
        Timer comm_timer;
        comm_timer.start();
        
        octetStream received_os;
        player.receive_player(1, received_os);

        comm_timer.stop();
        std::cout << "Receiving client's public key share time: " << comm_timer.elapsed() * 1e3 << " ms" << std::endl;

        // Unpack P_2's public key
        P256Element alphajG;
        alphajG.unpack(received_os);

        // Calculate the sum of P_1's and P_2's public keys
        P256Element alphaG = alphaiG + alphajG;

        // Timing beta_G generation and sending
        Timer beta_timer;
        beta_timer.start();
        P256Element::Scalar beta;
        beta.randomize(G);
        betaG = P256Element(beta);
        beta_timer.stop();
        std::cout << "Server Public Key Generation Time: " << beta_timer.elapsed() * 1e3 << " ms" << std::endl;

        Timer beta_send_timer;
        beta_send_timer.start();
        octetStream beta_os;
        betaG.pack(beta_os);
        player.send_to(1, beta_os);
        beta_send_timer.stop();
        std::cout << "Server Public Key Send Time: " << beta_send_timer.elapsed() * 1e3 << " ms" << std::endl;

        // Compute the product of `alphai` with `betaG`
        product = alphai * betaG;

        // Output P_1's and P_2's public keys along with their sum
        std::cout << "P_1's Public Key: " << alphaiG << std::endl;
        std::cout << "P_2's Public Key (Received): " << alphajG << std::endl;
        std::cout << "Combined Public Key: " << alphaG << std::endl;
    } else {
        // P_2 (Player 1) will send its public key to P_1
        Timer comm_timer;
        comm_timer.start();
        player.send_to(0, os);
        comm_timer.stop();
        std::cout << "Sending client's public key share time: " << comm_timer.elapsed() * 1e3 << " ms" << std::endl;

        // Output P_2's own public key
        std::cout << "P_2's Public Key: " << alphaiG << std::endl;

        // Receive `betaG` from P_1
        Timer beta_recv_timer;
        beta_recv_timer.start();
        octetStream beta_os;
        player.receive_player(0, beta_os);
        beta_recv_timer.stop();
        std::cout << "Server Public Key Receive Time: " << beta_recv_timer.elapsed() * 1e3 << " ms" << std::endl;

        // Unpack `betaG`
        betaG.unpack(beta_os);

        // Compute the product of `alphai` with `betaG`
        product = alphai * betaG;
    }

    // Output the server's public key and the party's key share
    std::cout << "Server Public Key: " << betaG << std::endl;
    std::cout << "Party's Combined Key Share: " << product << std::endl;

    // Finish curve parameters
    P256Element::finish();
}

