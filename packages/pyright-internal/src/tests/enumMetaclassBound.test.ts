/*
 * Copyright (c) Microsoft Corporation.
 * Licensed under the MIT license.
 *
 * Class-object bounds on metaclass instance methods.
 */

import * as TestUtils from './testUtils';

test('EnumMetaclassClassBoundPositive', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['enumMetaclassBoundPositive.py']);
    TestUtils.validateResults(results, 0);
});

test('EnumMetaclassClassBoundNegative', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['enumMetaclassBoundNegative.py']);
    TestUtils.validateResults(results, 5);
});

test('EnumMetaclassBroadBoundDoesNotGuaranteeOwner', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['enumMetaclassBoundBroad.py']);
    TestUtils.validateResults(results, 1);
});

test('GeneralMetaclassClassBoundAndExplicitSuperPositive', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['metaclassOwnerBoundPositive.py']);
    TestUtils.validateResults(results, 0);
});

test('GeneralMetaclassClassBoundAndExplicitSuperNegative', () => {
    const results = TestUtils.typeAnalyzeSampleFiles(['metaclassOwnerBoundNegative.py']);
    TestUtils.validateResults(results, 13);
});
