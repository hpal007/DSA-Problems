#![allow(dead_code)]

mod array {
    pub mod solutions;
    // problem 1
    // pub fn run(){
    //     let matrix = vec![vec![1,2,3],vec![4,5,6],vec![7,8,9]];
    //     let output_matrix = solutions::transpose(matrix);
    //     println!("{output_matrix:?}");
    // }

    // problem 2
    // pub fn run (){
    //     let input = vec![-4,-1,0,3,10];
    //     let output = solutions::sorted_squares(input);
    //     println!("{output:?}");
    // }

    // problem 3
    // pub fn run (){
    //     let mut nums1 = vec![1,2,3,0,0,0];
    //     let m = 3;
    //     let mut nums2 = vec![2,5,6];
    //     let n = 3;
    //     let output = solutions::merge_sorted_array(&mut nums1, m, &mut nums2, n);
    //     println!("{output:?}");
    // }

    // problem 4
    // pub fn run() {
    //     let mut nums = vec![0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
    //     let output = solutions::remove_duplicates(&mut nums);
    //     println!("{output:?}")
    // }

    // problem 5
    // pub fn run() {
    //     let mut nums = vec![0,1,2,2,3,0,4,2];
    //     let val = 2;
    //     let output = solutions::remove_element(&mut nums, val);
    //     println!("{output:?}")
    // }
    pub fn run() {
        let s = String::from("babad");
        let output = solutions::longest_palindrome(&s);
        println!("{output:?}")
    }
}

fn main() {
    array::run()
}
