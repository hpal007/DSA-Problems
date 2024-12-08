#![allow(dead_code)]

use problems::arrays;

mod problems {
    pub mod arrays;
}

fn main() {
    let input = vec![-4, -1, 0, 3, 10];
    let op = arrays::sorted_squares::sorted_squares(input);
    println!("{op:?}")
}
