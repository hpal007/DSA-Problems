// Solution for problem 1: Transpose of 
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

// Solution for problem 2: Square of sorted arrays
pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
    let mut output: Vec<i32> = Vec::new();
    for num in nums {
        output.push(num * num)
    }

    output.sort();
    output
}
