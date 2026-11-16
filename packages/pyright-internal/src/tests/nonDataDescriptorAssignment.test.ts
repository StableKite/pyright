/*
 * Copyright (c) Microsoft Corporation.
 * Licensed under the MIT license.
 *
 * Instance writes shadow non-data descriptors without rebinding the replacement.
 */

import * as assert from 'assert';

import * as TestUtils from './testUtils';

test('NonDataDescriptorAssignmentPositive', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['nonDataDescriptorAssignment1.py']);
    TestUtils.validateResults(results, 0);
});

test('NonDataDescriptorAssignmentNegative', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['nonDataDescriptorAssignment2.py']);
    const lines = TestUtils.readSampleFile('nonDataDescriptorAssignment2.py').split('\n');
    const expectedLines = lines.flatMap((line, index) => (line.includes('# error:') ? [index] : []));
    const actualLines = results.flatMap((result) => result.errors.map((error) => error.range.start.line));
    assert.deepStrictEqual(
        actualLines.sort((a, b) => a - b),
        expectedLines
    );
    TestUtils.validateResults(results, expectedLines.length);
});

test('NonDataDescriptorDeclaredAndInferredNegative', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['nonDataDescriptorAssignment3.py']);
    assert.deepStrictEqual(
        results[0].errors.map((error) => ({ line: error.range.start.line + 1, rule: error.getRule() })),
        [13, 14, 18, 19].map((line) => ({ line, rule: 'reportAttributeAccessIssue' }))
    );
    TestUtils.validateResults(results, 4);
});
