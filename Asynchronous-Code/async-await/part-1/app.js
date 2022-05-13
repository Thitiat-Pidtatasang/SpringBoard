let favNum = 5;
let baseURL = "http://numbersapi.com";

async function part1() {
    let data = await $.getJSON(`${baseURL}/${favNum}?json`);
    console.log(data);
}
part1();


const favNums = [6, 12, 22];
async function part2(){
    let data = await $.getJSON(`${baseURL}/${favNumbers}?json`);
    console.log(data);
}
part2();


async function part3() {
    let facts = await Promise.all(
        Array.from({ length: 4}, () => $.getJSON(`${baseURL}/${favNum}?json`))
    );
    facts.forEach(data => {
        $('body').append(`<p>${data.text}</p>`);
    });
}
part3();