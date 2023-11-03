// K번째수
// https://school.programmers.co.kr/learn/courses/30/lessons/42748

function solution(array, commands) {
  let answer = [];

  for(let i = 0; i < commands.length; i++) {
    let slicearr = array.slice(commands[i][0]-1, commands[i][1]).sort((a, b) => a - b)
    answer.push(slicearr[commands[i][2]-1])
  }

  return answer;
}

console.log(
  solution(
    [1, 5, 2, 6, 3, 7, 4],
    [
      [2, 5, 3],
      [4, 4, 1],
      [1, 7, 3],
    ]
  )
);
