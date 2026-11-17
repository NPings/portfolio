/* Shared behavior for the three discipline landing pages (R15, R24, R26).
   Everything is in memory for the life of the tab: nothing is stored or sent.
   Every count (chips, roles, sections, cards) is read from the DOM. */
(function () {
  /* The per-discipline session-notes copy. Single source: docs/portfolio-restructure-PRD.md section 20.5.
     Check with: python3 docs/tools/voicecheck.py assets/js/site.js */
/*VOICES-BEGIN*/
var VOICES = {
  "research-operations": {
    "panelTitle": "Study #1 · Field Notes",
    "panelTitleDone": "Study #1 · Field Report",
    "debriefLabel": "Field status",
    "debriefNote": "I run studies for a living, so this visit got fielded like one: recruited, scheduled, and thanked. Nothing above is about how well you did. It was measured in this tab alone, is stored nowhere, and disappears when you leave.",
    "events": {
      "open": "Field status: live. Recruitment: 1 of 1, quota met.",
      "hero": "Participant arrived on time. No-show rate: 0%.",
      "sections": {
        "Philosophy": "Participant reaches Philosophy. No consent form needed. Nothing here is recorded.",
        "Practice": "Participant reaches Practice. Four principles, straight from the research playbook.",
        "Selected Work": "Participant reaches the case studies. {cards} to choose from. Scheduling is flexible.",
        "Impact": "Impact numbers in view. Coded, tagged, and filed in the repository.",
        "Experience": "Participant reaches Experience. Rows open on request. No booking link required.",
        "Methods": "Methods board in view. Every card tagged and filed. Repository hygiene: excellent.",
        "Tools": "Tools marquee in view. Every one of these has sent me a renewal notice.",
        "Debrief": "Participant reaches the debrief. Session wrapped, right on schedule."
      },
      "sectionFallback": "Participant reaches {name}. Right on schedule.",
      "depth50": "Halfway through the session. Running on time.",
      "method1": "First method opened: \"{label}\". Logged to the repository.",
      "method5": "Five methods opened. This participant would be great for the panel.",
      "methodAll": "All {mTotal} methods opened. Somebody get this participant an incentive.",
      "role": "Participant opens {role}. Task completed, no facilitator needed.",
      "idle": "Participant pauses. Bio break, probably. The session will wait.",
      "return": "Participant is back. No need to reschedule."
    },
    "debrief": [
      {
        "cls": "note-head",
        "cases": [
          [
            "always",
            "Field report. Closing out the study."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "long",
            "Session length: {time}. Ran long. Good sessions usually do."
          ],
          [
            "always",
            "Session length: {time}. Wrapped early. The calendar appreciates it."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "full",
            "Protocol coverage: {seen} of {total} sections. Full protocol, no deviations."
          ],
          [
            "always",
            "Protocol coverage: {seen} of {total} sections. A few went by quickly. Unmoderated sessions are like that."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "methods5",
            "Methods opened: {mN} of {mTotal} ({mNames}). Rich data."
          ],
          [
            "methodsAny",
            "Methods opened: {mN} of {mTotal} ({mNames}). Useful data."
          ],
          [
            "always",
            "Methods opened: none. Observation-only is a valid study design."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "rolesAny",
            "Roles opened: {rN} of {rTotal} ({rNames}). Follow-up questions welcome."
          ],
          [
            "always",
            "Roles opened: none. The summary was enough to go on."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "pausesAny",
            "Breaks taken: {pN}. Participant wellbeing comes first."
          ],
          [
            "always",
            "Breaks taken: 0. Powered straight through."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "always",
            "No-show rate: 0%. Panel health: n=1, feeling great about it."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "always",
            "Incentive: good vibes only. The budget request is still pending."
          ]
        ]
      },
      {
        "cls": "",
        "cases": [
          [
            "always",
            "Recommendation: Get in touch to schedule a follow-up. The details are just above this panel."
          ]
        ]
      },
      {
        "cls": "note-head",
        "cases": [
          [
            "always",
            "Study closed. Thank you for participating. Nothing was recorded, and nothing leaves this tab."
          ]
        ]
      }
    ]
  },
  "consumer-research": {
    "panelTitle": "Participant #1 · Session Notes",
    "panelTitleDone": "Participant #1 · Session Debrief",
    "debriefLabel": "Your session",
    "debriefNote": "Every visit here is a small usability session. I observe it the way I'd observe any study, with the same respect for the participant. Everything above was measured in this tab alone, is stored nowhere, and disappears when you leave.",
    "events": {
      "open": "Session begins. One participant, unmoderated.",
      "hero": "Participant reads the hero. Or skims it. No judgment.",
      "sections": {
        "Philosophy": "Participant reaches Philosophy. Reading pattern assumed F-shaped.",
        "Practice": "Participant reaches Practice. Four principles, no pop quiz.",
        "Selected Work": "Participant reaches the case studies. {cards} to choose from.",
        "Impact": "Impact numbers in view. No need to catch them all.",
        "Experience": "Participant reaches Experience. The rows open if you want the details.",
        "Methods": "Methods board in view. The cards sorted themselves.",
        "Tools": "Tools marquee observed. It doesn't stop. Neither does research.",
        "Debrief": "Participant reaches the debrief. Full scroll achieved."
      },
      "sectionFallback": "Participant reaches {name}.",
      "depth50": "Halfway down the page. Engagement looks healthy.",
      "method1": "First method opened: \"{label}\". Curiosity confirmed.",
      "method5": "Five methods explored. A thorough participant.",
      "methodAll": "All {mTotal} methods opened. Above and beyond.",
      "role": "Participant expands {role}. Task success.",
      "idle": "Participant pauses. Thinking, or getting coffee.",
      "return": "Participant returns. Welcome back."
    },
    "debrief": [
      {
        "cls": "note-head",
        "cases": [
          [
            "always",
            "Debrief. Synthesizing the session while it is still fresh."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "long",
            "Duration: {time}. A considered read. Coffee may have been involved."
          ],
          [
            "always",
            "Duration: {time}. Brisk. The participant knows what they came for."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "full",
            "Coverage: {seen} of {total} sections reached. Complete. Every task attempted."
          ],
          [
            "always",
            "Coverage: {seen} of {total} sections reached. A few went by quickly. Skimming counts."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "methods5",
            "Methods opened: {mN} of {mTotal} ({mNames}). A hands-on participant."
          ],
          [
            "methodsAny",
            "Methods opened: {mN} of {mTotal} ({mNames}). Selective. Respect."
          ],
          [
            "always",
            "Methods opened: none. The board reads fine sorted, too."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "rolesAny",
            "Roles expanded: {rN} of {rTotal} ({rNames}). The details were wanted."
          ],
          [
            "always",
            "Roles expanded: none. The headlines cover the basics."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "pausesAny",
            "Pauses observed: {pN}. Reflection, or a second tab. Both are valid."
          ],
          [
            "always",
            "Pauses observed: 0. Momentum held the whole way."
          ]
        ]
      },
      {
        "cls": "",
        "cases": [
          [
            "always",
            "Finding 1: The participant made it to the end. Content held attention, which is the whole point."
          ]
        ]
      },
      {
        "cls": "",
        "cases": [
          [
            "clickedAny",
            "Finding 2: The participant clicked things. Interest moved from passive to active."
          ],
          [
            "always",
            "Finding 2: The participant read rather than clicked. A reader, not a clicker."
          ]
        ]
      },
      {
        "cls": "",
        "cases": [
          [
            "always",
            "Recommendation: Get in touch. The details are just above this panel."
          ]
        ]
      },
      {
        "cls": "note-head",
        "cases": [
          [
            "always",
            "Session closed. Thank you for participating. Nothing was recorded, and nothing leaves this tab."
          ]
        ]
      }
    ]
  }
};
/*VOICES-END*/

  var VOICE = VOICES[document.body.dataset.voice];
  document.body.classList.add('loaded');

  /* ---------- small helpers ---------- */
  var WORDS = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight'];
  function fill(text, vars) {
    return text.replace(/\{(\w+)\}/g, function (m, k) { return vars[k] === undefined ? '' : String(vars[k]); });
  }
  function joinNames(names, max) {
    var shown = names.slice(0, max).join(', ');
    return names.length > max ? shown + ', and ' + (names.length - max) + ' more' : shown;
  }
  function setText(id, text) {
    var el = document.getElementById(id);
    if (el) el.textContent = text;
  }

  /* ---------- methods board scatter ---------- */
  var chips = document.querySelectorAll('.chip');
  var chipTotal = chips.length;
  var seed = 11;
  function rnd() { seed = (seed * 1103515245 + 12345) % 2147483648; return seed / 2147483648; }
  chips.forEach(function (chip, i) {
    chip.style.setProperty('--i', i);
    chip.style.setProperty('--dx', ((rnd() - 0.5) * 110).toFixed(1) + 'px');
    chip.style.setProperty('--dy', (34 + rnd() * 110).toFixed(1) + 'px');
    chip.style.setProperty('--r', ((rnd() - 0.5) * 8).toFixed(1) + 'deg');
  });
  var board = document.getElementById('board');
  if (board && 'IntersectionObserver' in window) {
    var boardIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { board.classList.add('sorted'); boardIO.disconnect(); } });
    }, { threshold: 0.12 });
    boardIO.observe(board);
  } else if (board) {
    board.classList.add('sorted');
  }

  /* ---------- marquees ---------- */
  /* repeat each set until one copy is wider than any likely screen, then double it;
     the track slides exactly one copy (-50%) and loops cleanly. Nodes are cloned, never parsed from strings. */
  document.querySelectorAll('.track').forEach(function (t) {
    var kids = Array.prototype.slice.call(t.children);
    var setWidth = t.scrollWidth;
    if (!kids.length || !setWidth) return;
    var span = Math.max(window.innerWidth, screen.width || 0, 1920) * 1.5;
    var reps = Math.max(1, Math.ceil(span / setWidth));
    var base = parseFloat(getComputedStyle(t).animationDuration) || 46;
    var frag = document.createDocumentFragment();
    for (var i = 0; i < reps * 2; i++) {
      kids.forEach(function (k) { frag.appendChild(k.cloneNode(true)); });
    }
    t.textContent = '';
    t.appendChild(frag);
    t.style.animationDuration = (base * reps) + 's';
  });

  /* ---------- roles: one open at a time ---------- */
  var roles = document.querySelectorAll('details.role');
  var roleTotal = roles.length;
  roles.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (d.open) roles.forEach(function (o) { if (o !== d) o.open = false; });
    });
  });
  setText('dMethods', '0 / ' + chipTotal);
  setText('dRoles', '0 / ' + roleTotal);

  if (VOICE) {
  var EV = VOICE.events;
  /* ================================================================
     THE OBSERVER: the page runs a small, fully local usability
     session on its reader. Nothing is stored; nothing leaves the tab.
     ================================================================ */
  var t0 = Date.now();
  var log = document.getElementById('observerLog');
  var counter = document.getElementById('observerCount');
  var panel = document.getElementById('observer');
  var toggle = document.getElementById('observerToggle');
  var title = document.querySelector('.observer-title');
  var noteCount = 0;
  var MAX_NOTES = 90;
  var cardWord = WORDS[document.querySelectorAll('#selected-work a.case-card').length] || '';

  function stamp() {
    var s = Math.floor((Date.now() - t0) / 1000);
    var m = Math.floor(s / 60);
    return m + ':' + String(s % 60).padStart(2, '0');
  }
  function note(text, kind) {
    if (!log || noteCount >= MAX_NOTES) return;
    noteCount++;
    var li = document.createElement('li');
    var t = document.createElement('span');
    t.className = 'note-t';
    t.textContent = stamp();
    var body = document.createElement('span');
    body.textContent = text;
    if (kind) li.className = kind;
    li.appendChild(t); li.appendChild(body);
    log.appendChild(li);
    log.scrollTop = log.scrollHeight;
    if (counter) counter.textContent = noteCount;
  }
  function setObserverOpen(open) {
    if (!panel || !toggle) return;
    panel.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.classList.toggle('obs-open', open);
  }
  if (toggle) {
    toggle.addEventListener('click', function () {
      setObserverOpen(!panel.classList.contains('open'));
    });
  }

  /* opening lines */
  var debriefed = false;
  if (title) title.textContent = VOICE.panelTitle;
  note(EV.open);
  setTimeout(function () { if (!debriefed) note(EV.hero); }, 6000);

  /* section observation */
  var seen = {};
  if ('IntersectionObserver' in window) {
    var secIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var name = e.target.getAttribute('data-obs');
        if (e.isIntersecting && name && !seen[name]) {
          seen[name] = true;
          note(fill(EV.sections[name] || EV.sectionFallback, { cards: cardWord, name: name }));
        }
      });
    }, { threshold: 0.3 });
    document.querySelectorAll('[data-obs]').forEach(function (s) { secIO.observe(s); });
  }

  /* scroll depth */
  var maxDepth = 0, halfNoted = false;
  function onScroll() {
    var doc = document.documentElement;
    var depth = Math.min(100, Math.round((doc.scrollTop + window.innerHeight) / doc.scrollHeight * 100));
    if (depth > maxDepth) maxDepth = depth;
    if (depth >= 50 && !halfNoted) { halfNoted = true; note(EV.depth50); }
    if (depth >= 98) runDebrief();
    setText('dDepth', maxDepth + '%');
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  /* methods explored */
  var methodSeen = {};
  var methodsOpened = 0;
  chips.forEach(function (chip) {
    chip.addEventListener('toggle', function () {
      if (!chip.open) return;
      var nameEl = chip.querySelector('.chip-name');
      var label = nameEl ? nameEl.textContent : 'a method';
      if (methodSeen[label]) return;
      methodSeen[label] = true;
      methodsOpened++;
      setText('dMethods', methodsOpened + ' / ' + chipTotal);
      var vars = { label: label, mTotal: chipTotal };
      if (methodsOpened === 1) note(fill(EV.method1, vars));
      else if (methodsOpened === 5) note(fill(EV.method5, vars));
      else if (methodsOpened === chipTotal) note(fill(EV.methodAll, vars));
    });
  });

  /* roles opened */
  var roleSeen = {};
  var rolesOpened = 0;
  roles.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open) return;
      var r = d.getAttribute('data-role');
      if (!r || roleSeen[r]) return;
      roleSeen[r] = true;
      rolesOpened++;
      setText('dRoles', rolesOpened + ' / ' + roleTotal);
      note(fill(EV.role, { role: r }));
    });
  });

  /* rage clicks (R26): only voices that define a "rage" event count them.
     A burst is 3+ clicks within 700ms, each within 30px of the first; one burst counts once. */
  var rageCount = 0;
  if (EV.rage) {
    var burst = [], burstCounted = false;
    document.addEventListener('click', function (e) {
      var now = Date.now();
      var c = { t: now, x: e.clientX || 0, y: e.clientY || 0 };
      var first = burst[0];
      if (!first || now - first.t > 700 || Math.abs(c.x - first.x) > 30 || Math.abs(c.y - first.y) > 30 ||
          Math.sqrt(Math.pow(c.x - first.x, 2) + Math.pow(c.y - first.y, 2)) > 30) {
        burst = [c];
        burstCounted = false;
        return;
      }
      burst.push(c);
      if (burst.length >= 3 && !burstCounted) {
        burstCounted = true;
        rageCount++;
        if (rageCount === 1) note(EV.rage);
      }
    });
  }

  /* idle + return */
  var idleTimer, idleNoted = false, idleCount = 0;
  function resetIdle() {
    clearTimeout(idleTimer);
    idleTimer = setTimeout(function () {
      if (!idleNoted) { idleNoted = true; idleCount++; note(EV.idle); }
    }, 30000);
  }
  ['scroll', 'click', 'touchstart', 'keydown', 'mousemove'].forEach(function (evt) {
    window.addEventListener(evt, function () { idleNoted = false; resetIdle(); }, { passive: true });
  });
  resetIdle();

  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'visible') note(EV['return']);
  });

  /* ---------- full-scroll debrief: the notes widen and get thorough ---------- */
  function runDebrief() {
    if (debriefed) return;
    debriefed = true;
    var methods = Object.keys(methodSeen), rolesSeen = Object.keys(roleSeen);
    var sectionsSeen = Object.keys(seen).length;
    var sectionTotal = document.querySelectorAll('[data-obs]').length;
    var conds = {
      always: true,
      long: Date.now() - t0 >= 120000,
      full: sectionsSeen >= sectionTotal,
      methodsAny: methods.length >= 1,
      methods5: methods.length >= 5,
      rolesAny: rolesSeen.length >= 1,
      pausesAny: idleCount >= 1,
      clickedAny: methods.length >= 1 || rolesSeen.length >= 1,
      rageAny: rageCount >= 1
    };
    var vars = {
      cards: cardWord, time: stamp(), seen: sectionsSeen, total: sectionTotal,
      mN: methods.length, mNames: joinNames(methods, 3), mTotal: chipTotal,
      rN: rolesSeen.length, rNames: joinNames(rolesSeen, 3), rTotal: roleTotal,
      pN: idleCount, rage: rageCount
    };
    var lines = VOICE.debrief.map(function (item) {
      for (var i = 0; i < item.cases.length; i++) {
        if (conds[item.cases[i][0]]) return [fill(item.cases[i][1], vars), item.cls];
      }
      return null;
    }).filter(Boolean);
    if (title) title.textContent = VOICE.panelTitleDone;
    if (panel) panel.classList.add('full');
    document.body.classList.add('obs-full');
    setObserverOpen(true);
    lines.forEach(function (l, i) {
      setTimeout(function () { note(l[0], l[1]); }, 500 + i * 650);
    });
  }

  /* time on page ticker */
  setInterval(function () { setText('dTime', stamp()); }, 1000);
  }
})();
