// 최소 직사각형
// https://school.programmers.co.kr/learn/courses/30/lessons/86491

function solution(sizes) {
  let width = [];
  let height = [];
  for(let i = 0; i < sizes.length; i++) {
    width.push(Math.max(...sizes[i]))
    height.push(Math.min(...sizes[i]))
  }
  return Math.max(...width) * Math.max(...height);
}

console.log(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
console.log(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	))
console.log(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))