// 의상
// https://school.programmers.co.kr/learn/courses/30/lessons/42578

function solution(clothes) {
  let answer = 1;
  let types = {};
  
  clothes.forEach((c) => types[c[1]] = (types[c[1]] || 0) + 1);

  for (const t in types) {
    answer *= types[t] + 1;
  }

  return answer - 1 ;
}

console.log(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
console.log(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))

