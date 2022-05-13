let favNum = 5;
let baseURL = "http://numbersapi.com";

$.getJSON(`${baseURL}/${favNum}?json`, function(data) {
    console.log(data);
});

let favNums = [6, 12, 22];
$.getJSON(`${baseURL}/${favNums}?json`, function(data) {
    console.log(data);
});

let facts = [];
$.getJSON(`${baseURL}/${favNumber}?json`, function(data) {
  facts.push(data.text);
  $.getJSON(`${baseURL}/${favNumber}?json`, function(data) {
    facts.push(data.text);
    $.getJSON(`${baseURL}/${favNumber}?json`, function(data) {
      facts.push(data.text);
      $.getJSON(`${baseURL}/${favNumber}?json`, function(data) {
        facts.push(data.text);
        facts.forEach(fact => {
          $("body").append(`<p>${fact}</p>`);
        });
      });
    });
  });
});