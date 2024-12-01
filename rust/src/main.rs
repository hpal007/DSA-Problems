#![allow(dead_code)]  

mod easy {
    pub mod solutions;

    // pub fn run(){
    //     let matrix = vec![vec![1,2,3],vec![4,5,6],vec![7,8,9]];
    //     let output_matrix = solutions::transpose(matrix);
    //     println!("{output_matrix:?}");
    // }

    pub fn run (){
        let input = vec![-4,-1,0,3,10];
        let output = solutions::sorted_squares(input);
        println!("{output:?}");
    }
}


fn main() {
   easy::run()
}
