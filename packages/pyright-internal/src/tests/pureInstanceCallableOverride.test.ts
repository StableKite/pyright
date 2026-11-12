/*
 * Regression tests for Pure instance callable override.
 * B: fix checker behavior; retain all existing precision and diagnostics.
 */

import * as assert from 'assert';

import { ConfigOptions } from '../common/configOptions';
import { DiagnosticRule } from '../common/diagnosticRules';
import { pythonVersion3_15 } from '../common/pythonVersion';
import { Uri } from '../common/uri/uri';
import * as TestUtils from './testUtils';

const cases: [string, DiagnosticRule[]][] = [
    ['abstract_method_field', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_concrete_self_return', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_extra_required', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_keyword_only_narrowing', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_missing_default', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_parameter_variance', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_protocol_name', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_protocol_payload', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_protocol_posonly', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_protocol_return', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_return_variance', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_self_return', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_slots_descriptor', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['callable_variable_keyword_contract', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['class_default_callable_object', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['class_method_instance_field', []],
    ['classvar_callable_object', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['complete_overloaded_callback', []],
    ['concrete_instance_and_class_clients', []],
    ['dunder_lookup_covariance', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['final_method_field', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['generic_alias_callback', []],
    ['incomplete_overloaded_callback', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['parameter_and_return_variance', []],
    ['self_callback_grandchild', []],
    ['static_method_instance_field', []],
    ['valid_keyword_only', []],
    ['valid_positional_only_rename', []],
    ['valid_open_generic', []],
    ['bad_fixed_integer_callable', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_fixed_integer_result', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['valid_open_generic_broader_parameter', []],
    ['valid_method_generic_alpha_rename', []],
    ['bad_method_generic_fixed_int', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['bad_method_generic_fixed_result', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['storage_pure_instance_positive', []],
    ['storage_pure_instance_direct_class_call_missing_receiver', [DiagnosticRule.reportCallIssue]],
    ['storage_pure_instance_correct_class_call', []],
    ['storage_pure_instance_class_assignment', [DiagnosticRule.reportAttributeAccessIssue]],
    ['storage_pure_instance_classmethod_assignment', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['regular_class_direct_class_call_without_receiver', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['regular_class_class_assignment', [DiagnosticRule.reportIncompatibleMethodOverride]],
    ['regular_class_classmethod_assignment', [DiagnosticRule.reportIncompatibleMethodOverride]],
];

for (const [name, rules] of cases) {
    test(`Pure instance callable override: ${name}`, () => {
        const options = new ConfigOptions(Uri.empty());
        options.defaultPythonVersion = pythonVersion3_15;
        options.initializeTypeCheckingMode('strict');
        const results = TestUtils.typeAnalyzeSampleFiles([`pureInstanceCallableOverride/${name}.py`], options);
        TestUtils.validateResults(results, rules.length);
        assert.deepStrictEqual(results[0].errors.map((diagnostic) => diagnostic.getRule()).sort(), [...rules].sort());
    });
}
