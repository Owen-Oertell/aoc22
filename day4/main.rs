use std::cmp::max;
use std::cmp::min;
use std::fs;

fn main() {
    // Input
    let contents = fs::read_to_string("input.txt").expect("Something went wrong reading the file");

    // array for each line
    let lines: Vec<&str> = contents.split_whitespace().collect();
    let mut overlapped = 0;

    for line in lines {
        let seg: Vec<&str> = line.split(",").collect();
        let seg0: Vec<&str> = seg[0].split("-").collect();
        let seg1: Vec<&str> = seg[1].split("-").collect();
        // convert to ints
        let x0 = seg0[0].parse::<i32>().unwrap();
        let y0 = seg0[1].parse::<i32>().unwrap();
        let x1 = seg1[0].parse::<i32>().unwrap();
        let y1 = seg1[1].parse::<i32>().unwrap();

        // check if overlapped (x0,y0) and (x1,y1)
        if (max(x0, y0) >= min(x1, y1)) || (max(x1, y1) <= min(x0, y0)) {
            overlapped += 1;
        }
    }

    println!("{}", overlapped);
}
