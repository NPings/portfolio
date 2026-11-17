/* Case pages: if ?from= is one of the three discipline slugs, point both back links at that page.
   Fixed allowlist, text set with textContent, nothing from the URL is ever used as markup or a URL. */
(function () {
  var NAMES = { 'ai-evaluations': 'AI Evaluations', 'research-operations': 'Research Operations', 'consumer-research': 'Consumer Research' };
  var m = /[?&]from=([^&#]*)/.exec(location.search);
  var from = m ? m[1] : '';
  if (!Object.prototype.hasOwnProperty.call(NAMES, from)) return;
  document.querySelectorAll('a.back, .case-foot > a').forEach(function (a) {
    a.setAttribute('href', from + '.html');
    var arrow = a.querySelector('.arrow');
    a.textContent = '';
    if (arrow) a.appendChild(arrow);
    a.appendChild(document.createTextNode(' Back to ' + NAMES[from]));
  });
})();
