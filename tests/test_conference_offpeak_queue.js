const assert = require('node:assert/strict');
global.window = {};
require('../app/workflows.runner.js');

const isPeak = window.DPRWorkflowRunner.__test.isConferencePeakTime;
const getLabel = window.DPRWorkflowRunner.__test.getConferenceOffPeakLabel;
const utc = value => new Date(`${value}Z`);

assert.equal(isPeak(utc('2026-09-21T00:59:00')), false); // 周一 08:59
assert.equal(isPeak(utc('2026-09-21T01:00:00')), true);  // 周一 09:00
assert.equal(isPeak(utc('2026-09-21T04:30:00')), true);  // 周一 12:30，中午仍延后
assert.equal(isPeak(utc('2026-09-21T09:59:00')), true);  // 周一 17:59
assert.equal(isPeak(utc('2026-09-21T10:00:00')), false); // 周一 18:00
assert.equal(isPeak(utc('2026-09-20T04:00:00')), false); // 周日 12:00
assert.equal(getLabel(), '18:10');

console.log('conference off-peak queue tests passed');
