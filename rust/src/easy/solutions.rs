

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
pub fn sorted_squares_1(nums: Vec<i32>) -> Vec<i32> {
    // simple way to do it with sort. 
    let mut output:Vec<i32> = Vec::new();
    for num in nums{
        output.push(num*num);
    }
    output.sort();
    output
}

pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
    let num_length = nums.len();
    let mut output: Vec<i32> = vec![0; num_length];

    let mut right = num_length - 1;
    let mut left = 0;
    let mut index = num_length - 1;

    while left <= right {
        let left_square = nums[left] * nums[left];
        let right_square = nums[right] * nums[right];

        if right_square > left_square {
            output[index] = right_square;
            right -= 1;
        } else {
            output[index] = left_square;
            left += 1;
        }
        
        index = index.saturating_sub(1); // because using index -=1 gives overflow err, this stops that warning selecting mininum value only not overflow.
        
    }
    
    output
}