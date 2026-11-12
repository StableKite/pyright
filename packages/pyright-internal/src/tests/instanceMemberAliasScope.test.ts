/*
 * Regression tests for Instance member alias scope.
 * B: fix checker behavior; retain all existing precision and diagnostics.
 */

import * as assert from 'assert';

import { ConfigOptions } from '../common/configOptions';
import { DiagnosticRule } from '../common/diagnosticRules';
import { pythonVersion3_15 } from '../common/pythonVersion';
import { Uri } from '../common/uri/uri';
import * as TestUtils from './testUtils';

const cases: [string, DiagnosticRule[]][] = [
    ['closed_identity', []],
    ['nested_identity', []],
    ['legacy_identity', []],
    ['closed_list_alias', []],
    ['closed_union_alias', []],
    ['class_generic_identity', []],
    ['method_typevar_argument', [DiagnosticRule.reportGeneralTypeIssues]],
    ['escaped_method_alias', [DiagnosticRule.reportGeneralTypeIssues, DiagnosticRule.reportGeneralTypeIssues]],
    ['wrong_assignment', [DiagnosticRule.reportAttributeAccessIssue]],
    ['bare_missing_arguments', [DiagnosticRule.reportMissingTypeArgument, DiagnosticRule.reportUnknownMemberType]],
    ['invalid_alias_bound', [DiagnosticRule.reportInvalidTypeForm, DiagnosticRule.reportUnknownMemberType]],
    ['invalid_alias_arity', [DiagnosticRule.reportInvalidTypeForm]],
];

for (const [name, rules] of cases) {
    test(`Instance member alias scope: ${name}`, () => {
        const options = new ConfigOptions(Uri.empty());
        options.defaultPythonVersion = pythonVersion3_15;
        options.initializeTypeCheckingMode('strict');
        const results = TestUtils.typeAnalyzeSampleFiles([`instanceMemberAliasScope/${name}.py`], options);
        TestUtils.validateResults(results, rules.length);
        assert.deepStrictEqual(results[0].errors.map((diagnostic) => diagnostic.getRule()).sort(), [...rules].sort());
    });
}
