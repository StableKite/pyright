/*
 * Copyright (c) Microsoft Corporation.
 * Licensed under the MIT license.
 */

import * as assert from 'assert';

import * as TestUtils from './testUtils';

test('InstanceMethodShadowSeparateViews', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['instanceMethodShadow1.py']);
    TestUtils.validateResults(results, 0);
});

test('InstanceMethodShadowProtocolsAndClassLookups', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['instanceMethodShadow2.py']);
    TestUtils.validateResults(results, 0);
});

test('InstanceMethodShadowInvalidCallsAndWritableContracts', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['instanceMethodShadow3.py']);
    const expected = TestUtils.readSampleFile('instanceMethodShadow3.py')
        .split('\n')
        .flatMap((line, index) => (line.includes('# error') ? [index + 1] : []));
    const actual = results[0].errors.map((error) => error.range.start.line + 1).sort((a, b) => a - b);
    assert.deepStrictEqual(actual, expected);
    TestUtils.validateResults(results, expected.length);
});

test('InstanceMethodShadowMutableBoundaries', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['instanceMethodShadow4.py']);
    const expected = TestUtils.readSampleFile('instanceMethodShadow4.py')
        .split('\n')
        .flatMap((line, index) => (line.includes('# error') ? [index + 1] : []));
    const actual = results[0].errors.map((error) => error.range.start.line + 1).sort((a, b) => a - b);
    assert.deepStrictEqual(actual, expected);
    TestUtils.validateResults(results, expected.length);
});

test('InstanceMethodShadowReadonlyBoundaries', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['instanceMethodShadow5.py']);
    const expected = TestUtils.readSampleFile('instanceMethodShadow5.py')
        .split('\n')
        .flatMap((line, index) => (line.includes('# readonly') ? [index + 1] : []));
    for (const line of expected) {
        assert.ok(
            results[0].errors.some(
                (error) => error.range.start.line + 1 === line && error.getRule() === 'reportAttributeAccessIssue'
            ),
            `Expected readonly assignment diagnostic at line ${line}`
        );
    }
});
