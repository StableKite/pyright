/*
 * Regression tests for callable instance attributes overriding methods.
 * Existing method, variable, descriptor and special-method checks stay intact.
 */

import * as assert from 'assert';

import { ConfigOptions } from '../common/configOptions';
import { DiagnosticRule } from '../common/diagnosticRules';
import { pythonVersion3_15 } from '../common/pythonVersion';
import { Uri } from '../common/uri/uri';
import * as TestUtils from './testUtils';

const cases: [string, number][] = [
    ['abstract_method_field', 1],
    ['bad_concrete_self_return', 1],
    ['bad_extra_required', 1],
    ['bad_keyword_only_narrowing', 1],
    ['bad_missing_default', 1],
    ['bad_parameter_variance', 1],
    ['bad_protocol_name', 1],
    ['bad_protocol_payload', 1],
    ['bad_protocol_posonly', 1],
    ['bad_protocol_return', 1],
    ['bad_return_variance', 1],
    ['bad_self_return', 1],
    ['bad_slots_descriptor', 1],
    ['callable_variable_keyword_contract', 1],
    ['class_default_callable_object', 1],
    ['class_method_instance_field', 0],
    ['classvar_callable_object', 1],
    ['complete_overloaded_callback', 0],
    ['concrete_instance_and_class_clients', 0],
    ['dunder_lookup_covariance', 1],
    ['final_method_field', 1],
    ['generic_alias_callback', 0],
    ['incomplete_overloaded_callback', 1],
    ['parameter_and_return_variance', 0],
    ['self_callback_grandchild', 0],
    ['static_method_instance_field', 0],
    ['valid_keyword_only', 0],
    ['valid_positional_only_rename', 0],
];

for (const [name, errors] of cases) {
    test(`Callable instance override: ${name}`, () => {
        const options = new ConfigOptions(Uri.empty());
        options.defaultPythonVersion = pythonVersion3_15;
        options.initializeTypeCheckingMode('strict');
        const results = TestUtils.typeAnalyzeSampleFiles([`callableInstanceOverride/${name}.py`], options);
        TestUtils.validateResults(results, errors);
        for (const diagnostic of results[0].errors) {
            assert.strictEqual(diagnostic.getRule(), DiagnosticRule.reportIncompatibleMethodOverride);
        }
    });
}
