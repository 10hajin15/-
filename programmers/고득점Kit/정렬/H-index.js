// H-index
// https://school.programmers.co.kr/learn/courses/30/lessons/42747

function solution(citations) {
  let answer = 0;
  for (let h = 1; h < Math.max(...citations); h++) {
    let count = 0;
    for (let j = 0; j < citations.length; j++) {
      if (h <= citations[j]) count += 1;
    }
    if (h <= count) answer = h;
    else return answer;
  }

  return answer;
}

console.log(solution([3, 0, 6, 1, 5]));
console.log(solution([3, 4]));
console.log(solution([4, 3, 3, 3, 0, 0, 0]));
