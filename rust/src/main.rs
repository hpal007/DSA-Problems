#![allow(dead_code)]  

mod easy {
    pub mod solutions;

    // pub fn run(){
    //     let matrix = vec![vec![1,2,3],vec![4,5,6],vec![7,8,9]];
    //     let output_matrix = solutions::transpose(matrix);
    //     println!("{output_matrix:?}");
    // }

    // pub fn run (){
    //     let input = vec![-4,-1,0,3,10];
    //     let output = solutions::sorted_squares(input);
    //     println!("{output:?}");
    // }


    pub fn run (){
        let mut nums1 = vec![1,2,3,0,0,0];
        let m = 3;
        let mut nums2 = vec![2,5,6];
        let n = 3;
        let output = solutions::merge_sorted_array(&mut nums1, m, &mut nums2, n);
        println!("{output:?}");
    }
}



fn main() {
   easy::run()
}
