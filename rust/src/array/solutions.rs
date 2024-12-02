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

// problem 2: Square of sorted arrays
pub fn sorted_squares_1(nums: Vec<i32>) -> Vec<i32> {
    // simple way to do it with sort.
    let mut output: Vec<i32> = Vec::new();
    for num in nums {
        output.push(num * num);
    }
    output.sort();
    output
}

// problem 2: Square of sorted arrays (better way to do it)
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

// problem 3: 88. merge sorted arrays
pub fn merge_sorted_array(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
    let mut i = m - 1; // pointer to last elment in nums1
    let mut j = n - 1; // pointer to last elment in nums2
    let mut k = (m + n) as usize - 1; // pointer to last elment in nums1 (total length)

    //  merge in reverse  order
    while i >= 0 && j >= 0 {
        if nums1[i as usize] > nums2[j as usize] {
            nums1[k] = nums1[i as usize];
            i -= 1;
        } else {
            nums1[k] = nums2[j as usize];
            j -= 1;
        }
        k -= 1;
    }
    //  Add remaining values from nums 2 if j is still not 0
    // This will happen when length of nums2 is greater then nums 1
    while j >= 0 {
        nums1[k] = nums2[j as usize];
        j -= 1;
        k -= 1
    }
    println!("{nums1:?}");
}

 // problem 4: 26. Remove Duplicates from Sorted Array
pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
    let mut u = 0;

    for i in 1..nums.len() {
        if nums[u] != nums[i] {
            u += 1;
            nums[u] = nums[i]
        }
    }
    println!("{nums:?}");

    return u as i32 + 1;
}
