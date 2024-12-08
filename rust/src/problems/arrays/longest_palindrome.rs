// problem 6
pub fn longest_palindrome(s: &str) -> String {
    let l = s.len();
    let mut ans = String::new();
    let mut maxlen = 0;

    // Check for odd-length palindromes
    for mid in 0..l {
        let (mut i, mut j) = (mid as isize, mid as isize);
        let mut curlen = 1;

        while i > 0
            && j < l as isize
            && s.chars().nth(i as usize - 1) == s.chars().nth(j as usize + 1)
        {
            i -= 1;
            j += 1;
            curlen += 2;
        }

        if curlen > maxlen {
            ans = s[i as usize..=j as usize].to_string();
            maxlen = curlen;
        }
    }

    // Check for even-length palindromes
    for mid in 0..l - 1 {
        let (mut i, mut j) = (mid as isize, mid as isize + 1);
        let mut curlen = 0;

        while i >= 0 && j < l as isize && s.chars().nth(i as usize) == s.chars().nth(j as usize) {
            i -= 1;
            j += 1;
            curlen += 2;
        }

        if curlen > maxlen {
            ans = s[i as usize + 1..=j as usize - 1].to_string();
            maxlen = curlen;
        }
    }

    ans
}

//     let s = String::from("babad");
