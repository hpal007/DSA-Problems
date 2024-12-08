// problem 1: Transpose of
pub fn transpose(matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    let r = matrix.len();
    let c = matrix[0].len();

    let mut output = vec![vec![0; r]; c];

    for i in 0..r {
        for j in 0..c {
            output[j][i] = matrix[i][j]
        }
    }

    output
}


//input  let matrix = vec![vec![1,2,3],vec![4,5,6],vec![7,8,9]];
