// problem 5: 27. Remove Element
pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
    let mut k = 0;

    for i in 0..nums.len() {
        if nums[i] != val {
            nums[k] = nums[i];
            k += 1
        }
    }
    println!("{nums:?}");
    k as i32
}

//     let mut nums = vec![0,1,2,2,3,0,4,2];
//     let val = 2;
