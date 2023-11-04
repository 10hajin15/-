// 모의고사
// https://school.programmers.co.kr/learn/courses/30/lessons/42840

function solution(answers) {
  let stu1 = [1, 2, 3, 4, 5];
  let stu2 = [2, 1, 2, 3, 2, 4, 2, 5];
  let stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  let score = [0,0,0];

  for (let i = 0; i < answers.length; i++) {
    if(answers[i] === stu1[Math.floor(i%stu1.length)]) {
      score[0] += 1
    }
    if(answers[i] === stu2[Math.floor(i%stu2.length)]) {
      score[1] += 1
    }
    if(answers[i] === stu3[Math.floor(i%stu3.length)]) {
      score[2] += 1
    }
  }

  let answer = []
  let maxScore = Math.max(...score);
  for(let i = 0; i < score.length; i++) {
    if(maxScore === score[i]) answer.push(i+1)
  }

  return answer;
}

console.log(solution([1, 2, 3, 4, 5]));
console.log(solution([1, 3, 2, 4, 2]));
