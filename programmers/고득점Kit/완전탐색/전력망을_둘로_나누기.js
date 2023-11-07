// 전력망을 둘로 나누기
// https://school.programmers.co.kr/learn/courses/30/lessons/86971

function solution(n, wires) {
  let answer = Number.MAX_SAFE_INTEGER;

  let tree = Array.from(Array(n + 1), () => []);
  wires.map((el) => {
    let [a, b] = el;
    tree[a].push(b);
    tree[b].push(a);
  });

  const searchTree = (root, exceptNum) => {
    let count = 0;
    let visit = [];
    let queue = [root];
    visit[root] = true;
    while (queue.length) {
      let index = queue.pop();
      tree[index].forEach((el) => {
        if (el !== exceptNum && visit[el] !== true) {
          visit[el] = true;
          queue.push(el);
        }
      });
      count++;
    }
    return count;
  };

  wires.forEach((el) => {
    let [a, b] = el;
    answer = Math.min(answer, Math.abs(searchTree(a, b) - searchTree(b, a)));
  });

  return answer;
}

console.log(
  solution(9, [
    [1, 3],
    [2, 3],
    [3, 4],
    [4, 5],
    [4, 6],
    [4, 7],
    [7, 8],
    [7, 9],
  ])
);
console.log(
  solution(4, [
    [1, 2],
    [2, 3],
    [3, 4],
  ])
);
console.log(
  solution(7, [
    [1, 2],
    [2, 7],
    [3, 7],
    [3, 4],
    [4, 5],
    [6, 7],
  ])
);
