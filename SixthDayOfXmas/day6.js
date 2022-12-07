let input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg";

let done;
[...input.trim()].forEach((x, i) => {
  const data = input.trim().slice(i - 3, i) + x;
  var unique = [...data].filter((v, i, s) => s.indexOf(v) === i);

  if (unique.length == 4 && !done) {
    done = i + 1;
    console.log(done, "points");
  }
});
