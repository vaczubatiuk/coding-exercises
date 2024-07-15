

fn DAG<T: Clone>(vec: &[T]) -> Vec<T> {
    let mut newVec = vec.to_vec();
    shuffle(&mut newVec);
    mergeSort(newVec);
}

fn mergeSort(vec: &[Vec<i32>], l: i32, r: i32) -> Vector<T> {
    let n = 1 + (r-1)/2;
    sortCheck(&vec,l,m);
    sortCheck(&vec,n+1,r);
    merging(&vec,1,n,r);

}
fn sortCheck(vec: &[Vec<i32>], l: i32, r: i32) {
    let mut comp = vec[r];
    if (vec[r][1] < vec[l][2]){
        vec[r] = vec[l];
        vec[l] = comp ;
    }
}

fn merging(vec: &[Vec<i32>], l: i32, n: i32, r: i32) {
    let idx1 = n+l-1;
    let idx2 = r-n;
    let mut Vec<i32> left = Vec::with_capacity(idx1 as usize);
    let mut Vec<i32> right = Vec::with_capacity(idx2 as usize);
    for i in 0..idx1 {
        left[i] = vec[l+i];
    }
    for i in 0..idx2 {
        right[i] = vec[m+1+i];
    }
    let mut a = 0;
    let mut b = 0;
    let mut c = l;
    while i < idx1 && j < idx2 {
        if left[i] <= right[j] {
            vec[k++] = left[i++]
        }
        else {
            vec[k++] = right[k++]
        }
    }
    while i < idx1 {
        vec[k++] = left[i++]
    }
    while i < idx2 {
        vec[k++] = right[i++]
    }
}


fn missileDefend(missile: &[Vec<i32>]) -> i32 {
    let mut dag = DAG(missile);
    let n = dag.len();
    let mut ypoint = new Vector<i32>.with_capacity(n as usize)
    for i in 0..n {
        ypoint.push(dag[n][1]);
    }
    results = new i32;

    for y in ypoint {
        
    }

}