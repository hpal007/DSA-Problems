pub fn rectangular_star_pattern(n: i32,m: i32) {
    // Problem Statement: Given an integer N, print the following pattern.
    //  * * * * *
    //  * * * * *
    //  * * * * *
    //  * * * * *

    for _ in 0..n{
        for _ in 0..m{
            print!("* ")
        }
        println!(" ")
    }
}