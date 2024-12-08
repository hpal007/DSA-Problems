pub fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
    let mut output: Vec<i32> = vec![];

    for i in 0..words.len() {
        if words[i].contains(x) {
            output.push(i as i32);
        }
    }

    return output;
}

//     let words: Vec<String> =vec!["abc".to_string(),"bcd".to_string(),"aaaa".to_string(),"cbc".to_string()];
//     let x: char = 'a';
