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

//     let mut nums = vec![0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
