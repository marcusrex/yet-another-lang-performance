<?php
    require_once(dirname(__FILE__).'/benchmarks/bad_benchmarks/primes_benchmark.php');
    require_once(dirname(__FILE__).'/benchmarks/bad_benchmarks/spectral_norm_benchmark.php');

    use Benchmarks\BadBenchmarks\PrimesBenchmark;
    use Benchmarks\BadBenchmarks\SpectralNormBenchmark;

    function print_results($results){
        echo PHP_EOL;
        foreach($results as $result){
            echo sprintf("Benchmark: %s Avg. elapsed time: %f Used mem: %d Avg Total Memory: %d Runs: %d \n",
             $result->name, $result->avg_elapsed_time, $result->used_mem, $result->total_used_mem, $result->run_number);
        }
        echo PHP_EOL;
    }

    $benchmarks = array(
        new PrimesBenchmark(),
        new SpectralNormBenchmark()
    );


    $benchmark_results = array();

    foreach($benchmarks as $benchmark){
        array_push($benchmark_results, $benchmark->execute());
    }

    print_results($benchmark_results)
?>