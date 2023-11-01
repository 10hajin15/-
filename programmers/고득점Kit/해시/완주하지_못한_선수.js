function solution(participant, completion) {
  let runner = new Map();

  for(let i = 0; i < participant.length; i++) {
    let a = participant[i];
    let b = completion[i];
    runner.set(a, (runner.get(a) || 0) + 1);
    runner.set(b, (runner.get(b) || 0) - 1);
  }

  for (let [key, value] of runner) {
    if(value > 0) return key;
  }

  return;
}

console.log(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))
console.log(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
console.log(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))