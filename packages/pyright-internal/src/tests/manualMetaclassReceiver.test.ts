/*
 * Copyright (c) Microsoft Corporation.
 * Licensed under the MIT license.
 */

import * as assert from 'assert';

import * as TestUtils from './testUtils';

test('ManualMetaclassReceiverPositive', () => {
    TestUtils.validateResults(TestUtils.typeAnalyzeSampleFiles(['manualMetaclassReceiver1.py']), 0);
});

test('ManualMetaclassReceiverWrongOwner', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['manualMetaclassReceiver2.py']);
    const expected = TestUtils.readSampleFile('manualMetaclassReceiver2.py')
        .split('\n')
        .flatMap((line, index) => (line.includes('# error') ? [index + 1] : []));
    const actual = results[0].errors.map((error) => error.range.start.line + 1).sort((a, b) => a - b);
    assert.deepStrictEqual(actual, expected);
    TestUtils.validateResults(results, expected.length);
});

test('ManualMetaclassReceiverGenericResultsAndStoredFields', () => {
    TestUtils.validateResults(TestUtils.typeAnalyzeSampleFiles(['manualMetaclassReceiver3.py']), 0);
});

test('ManualMetaclassReceiverUnprovedGenericAndKeywordOnly', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['manualMetaclassReceiver4.py']);
    const expected = TestUtils.readSampleFile('manualMetaclassReceiver4.py')
        .split('\n')
        .flatMap((line, index) => (line.includes('# error') ? [index + 1] : []));
    const actual = results[0].errors.map((error) => error.range.start.line + 1).sort((a, b) => a - b);
    assert.deepStrictEqual(actual, expected);
    TestUtils.validateResults(results, expected.length);
});
