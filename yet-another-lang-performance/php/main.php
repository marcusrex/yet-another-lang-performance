<?php
    include dirname(__FILE__).'/benchmarks/bad_benchmarks/primes_benchmark.php';

    use Benchmarks\BadBenchmarks\PrimesBenchmark;

    function print_results($results){
        foreach($results as $result){
            echo sprintf("Benchmark: %s Avg. elapsled time: %f Runs: %d", $result->name, $result->avg_elapsed_time, $result->run_number);
        }
    }

    $benchmarks = array(
        new PrimesBenchmark()
    );


    $benchmark_results = array();

    foreach($benchmarks as $benchmark){
        array_push($benchmark_results, $benchmark->execute());
    }

    print_results($benchmark_results)
?>