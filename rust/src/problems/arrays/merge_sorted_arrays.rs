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

// input
//     let mut nums1 = vec![1,2,3,0,0,0];
//     let m = 3;
//     let mut nums2 = vec![2,5,6];
//     let n = 3;
