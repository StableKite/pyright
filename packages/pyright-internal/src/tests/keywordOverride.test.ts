/*
 * Copyright (c) Microsoft Corporation.
 * Licensed under the MIT license.
 * Regression tests for keyword-only parameters implemented as standard parameters.
 */

import * as assert from 'assert';

import { ConfigOptions } from '../common/configOptions';
import { Uri } from '../common/uri/uri';
import * as TestUtils from './testUtils';

test('KeywordOverrideOptionalStandard', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideOptionalStandard.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideOptionalReordered', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideOptionalReordered.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideOptionalInterleaved', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideOptionalInterleaved.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideRequiredStandard', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideRequiredStandard.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideRequiredReordered', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideRequiredReordered.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideRequiredToOptional', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideRequiredToOptional.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideRequiredMixed', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideRequiredMixed.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideWithPrefix', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideWithPrefix.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideWithPositionalOnlyPrefix', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideWithPositionalOnlyPrefix.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideKeywordControl', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideKeywordControl.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideMissingKeyword', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideMissingKeyword.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverrideWrongTypeStandard', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideWrongTypeStandard.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverrideWrongTypeKeyword', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideWrongTypeKeyword.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverrideWrongTypeReordered', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideWrongTypeReordered.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverrideLostDefaults', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideLostDefaults.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverrideExtraRequired', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideExtraRequired.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverridePositionalOnlyRestriction', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverridePositionalOnlyRestriction.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverrideReverseRestriction', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideReverseRestriction.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverrideStandardOrderRestriction', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideStandardOrderRestriction.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverrideStatic', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideStatic.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideClass', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideClass.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideGeneric', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideGeneric.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideProtocolStandard', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideProtocolStandard.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideProtocolReordered', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideProtocolReordered.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverrideProtocolMissing', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideProtocolMissing.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [11]
    );
});

test('KeywordOverrideProtocolWrongType', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideProtocolWrongType.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [11]
    );
});

test('KeywordOverrideProtocolPositionalOnly', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideProtocolPositionalOnly.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [11]
    );
});

test('KeywordOverridePlainCallableStandard', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverridePlainCallableStandard.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverridePlainCallableKeywordRestriction', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverridePlainCallableKeywordRestriction.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverridePlainCallableWrongType', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverridePlainCallableWrongType.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverrideOccupiedPosition', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideOccupiedPosition.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverrideOccupiedPositionWithKwargs', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideOccupiedPositionWithKwargs.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverrideVariadicCollision', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideVariadicCollision.py'], options);
    TestUtils.validateResults(results, 1);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        [7]
    );
});

test('KeywordOverrideNeverVariadic', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverrideNeverVariadic.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});

test('KeywordOverridePositionalOnlyWithKeywordSink', () => {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    const results = TestUtils.typeAnalyzeSampleFiles(['keywordOverridePositionalOnlyWithKeywordSink.py'], options);
    TestUtils.validateResults(results, 0);
    assert.deepStrictEqual(
        results[0].errors.map((diag) => diag.range.start.line + 1),
        []
    );
});
