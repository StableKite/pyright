/*
 * Copyright (c) Microsoft Corporation.
 * Licensed under the MIT license.
 * Constructor results follow the evaluated __new__ and metaclass __call__.
 */

import * as assert from 'assert';

import { ConfigOptions } from '../common/configOptions';
import { Uri } from '../common/uri/uri';
import * as TestUtils from './testUtils';

function analyze(file: string) {
    const options = new ConfigOptions(Uri.empty());
    options.initializeTypeCheckingMode('strict');
    options.defaultPythonVersion = { major: 3, minor: 15 };
    options.diagnosticRuleSet.reportInconsistentConstructor = 'error';
    return TestUtils.typeAnalyzeSampleFiles([file], options);
}

test('ConstructorNewResultPrimaryPositive', () => {
    const results = analyze('constructorNewResultPrimaryPositive.py');
    TestUtils.validateResults(results, 0);
});

test('ConstructorNewResultPrimaryNegative', () => {
    const results = analyze('constructorNewResultPrimaryNegative.py');
    TestUtils.validateResults(results, 7);
    assert.deepStrictEqual(
        results[0].errors
            .slice()
            .sort((a, b) => a.range.start.line - b.range.start.line)
            .map((diag) => [diag.range.start.line + 1, diag.getRule()]),
        [
            [3, 'reportUnusedImport'],
            [37, 'reportArgumentType'],
            [38, 'reportCallIssue'],
            [38, 'reportCallIssue'],
            [39, 'reportArgumentType'],
            [40, 'reportArgumentType'],
            [45, 'reportReturnType'],
        ]
    );
});

test('ConstructorNewResultStandardPositive', () => {
    const results = analyze('constructorNewResultStandardPositive.py');
    TestUtils.validateResults(results, 0);
});

test('ConstructorNewResultStandardNegative', () => {
    const results = analyze('constructorNewResultStandardNegative.py');
    TestUtils.validateResults(results, 10);
    assert.deepStrictEqual(
        results[0].errors
            .slice()
            .sort((a, b) => a.range.start.line - b.range.start.line)
            .map((diag) => [diag.range.start.line + 1, diag.getRule()]),
        [
            [18, 'reportArgumentType'],
            [26, 'reportGeneralTypeIssues'],
            [34, 'reportArgumentType'],
            [45, 'reportArgumentType'],
            [45, 'reportArgumentType'],
            [53, 'reportAbstractUsage'],
            [58, 'reportReturnType'],
            [69, 'reportInconsistentConstructor'],
            [73, 'reportArgumentType'],
            [78, 'reportArgumentType'],
        ]
    );
});
