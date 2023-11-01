// 폰켓몬
// https://school.programmers.co.kr/learn/courses/30/lessons/1845

function solution(nums) {
  let setNums = new Set(nums);
  if((nums.length/2) > setNums.size) return setNums.size;
  return nums.length/2
}

console.log(solution([3,1,2,3]))
console.log(solution([3,3,3,2,2,4]))
console.log(solution([3,3,3,2,2,2]))