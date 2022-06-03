from parse.tokenizer import Tokenizer

sql = """SELECT AbsenceAgreementDEO.ABSENCE_AGREEMENT_ID, AbsenceAgreementDEO.ENTERPRISE_ID, AbsenceAgreementDEO.LEGISLATION_CODE, 
AbsenceAgreementDEO.EFFECTIVE_START_DATE, AbsenceAgreementDEO.EFFECTIVE_END_DATE, AbsenceAgreementDEO.ANC_ABSENCE_AGREEMENTS_F_ALTCD, 
AbsenceAgreementTranslationDEO.NAME, AbsenceAgreementTranslationDEO.DESCRIPTION, AbsenceAgreementTranslationDEO.LANGUAGE, AbsenceAgreementDEO.MANAGEMENT_TYPE_CD, 
AbsenceAgreementDEO.STATUS, AbsenceAgreementDEO.PARTNER_RULE_CD, AbsenceAgreementDEO.AGREEMENT_PATTERN_CD, AbsenceAgreementDEO.LEG_GROUPING_CD, 
AbsenceAgreementDEO.ABSENCE_TYPE_ID, AbsenceAgreementDEO.ELIGI_FORMULA_ID, AbsenceAgreementDEO.ELIGI_PROFILE_ID, AbsenceAgreementDEO.ELIGI_OVERRIDE_CD, 
AbsenceAgreementDEO.ELIGI_RULE_CD, AbsenceAgreementDEO.DENIAL_REASON_CD, AbsenceAgreementDEO.WITHDRAW_REASON_CD, AbsenceAgreementDEO.VALIDATION_FORMULA_ID, 
AbsenceAgreementDEO.OBJECT_VERSION_NUMBER, AbsenceAgreementDEO.CREATED_BY, AbsenceAgreementDEO.CREATION_DATE, AbsenceAgreementDEO.LAST_UPDATED_BY, 
AbsenceAgreementDEO.LAST_UPDATE_DATE, AbsenceAgreementDEO.LAST_UPDATE_LOGIN, AbsenceAgreementTranslationDEO.SOURCE_LANG, AbsenceAgreementDEO.ANC_CHAR1, 
AbsenceAgreementDEO.ANC_CHAR2, AbsenceAgreementDEO.ANC_CHAR3, AbsenceAgreementDEO.ANC_CHAR4, AbsenceAgreementDEO.ANC_CHAR5, AbsenceAgreementDEO.ANC_NUMBER1, 
AbsenceAgreementDEO.ANC_NUMBER2, AbsenceAgreementDEO.ANC_NUMBER3, AbsenceAgreementDEO.ANC_NUMBER4, AbsenceAgreementDEO.ANC_NUMBER5, AbsenceAgreementDEO.ANC_DATE1, 
AbsenceAgreementDEO.ANC_DATE2, AbsenceAgreementDEO.ANC_DATE3, AbsenceAgreementDEO.ANC_DATE4, AbsenceAgreementDEO.ANC_DATE5, AbsenceAgreementDEO.MODULE_ID, 
AbsenceAgreementDEO.INFORMATION_CATEGORY, AbsenceAgreementDEO.INFORMATION1, AbsenceAgreementDEO.INFORMATION2, AbsenceAgreementDEO.INFORMATION3, 
AbsenceAgreementDEO.INFORMATION4, AbsenceAgreementDEO.INFORMATION5, AbsenceAgreementDEO.INFORMATION6, AbsenceAgreementDEO.INFORMATION7, AbsenceAgreementDEO.INFORMATION8, 
AbsenceAgreementDEO.INFORMATION9, AbsenceAgreementDEO.INFORMATION10, AbsenceAgreementDEO.INFORMATION11, AbsenceAgreementDEO.INFORMATION12, AbsenceAgreementDEO.INFORMATION13, 
AbsenceAgreementDEO.INFORMATION14, AbsenceAgreementDEO.INFORMATION15, AbsenceAgreementDEO.INFORMATION16, AbsenceAgreementDEO.INFORMATION17, AbsenceAgreementDEO.INFORMATION18, 
AbsenceAgreementDEO.INFORMATION19, AbsenceAgreementDEO.INFORMATION20, AbsenceAgreementDEO.INFORMATION21, AbsenceAgreementDEO.INFORMATION22, AbsenceAgreementDEO.INFORMATION23, 
AbsenceAgreementDEO.INFORMATION24, AbsenceAgreementDEO.INFORMATION25, AbsenceAgreementDEO.INFORMATION26, AbsenceAgreementDEO.INFORMATION27, AbsenceAgreementDEO.INFORMATION28, 
AbsenceAgreementDEO.INFORMATION29, AbsenceAgreementDEO.INFORMATION30, AbsenceAgreementDEO.ATTRIBUTE_CATEGORY, AbsenceAgreementDEO.ATTRIBUTE1, AbsenceAgreementDEO.ATTRIBUTE2, 
AbsenceAgreementDEO.ATTRIBUTE3, AbsenceAgreementDEO.ATTRIBUTE4, AbsenceAgreementDEO.ATTRIBUTE5, AbsenceAgreementDEO.ATTRIBUTE6, AbsenceAgreementDEO.ATTRIBUTE7, 
AbsenceAgreementDEO.ATTRIBUTE8, AbsenceAgreementDEO.ATTRIBUTE9, AbsenceAgreementDEO.ATTRIBUTE10, AbsenceAgreementDEO.ATTRIBUTE11, AbsenceAgreementDEO.ATTRIBUTE12, 
AbsenceAgreementDEO.ATTRIBUTE13, AbsenceAgreementDEO.ATTRIBUTE14, AbsenceAgreementDEO.ATTRIBUTE15, AbsenceAgreementDEO.ATTRIBUTE16, AbsenceAgreementDEO.ATTRIBUTE17, 
AbsenceAgreementDEO.ATTRIBUTE18, AbsenceAgreementDEO.ATTRIBUTE19, AbsenceAgreementDEO.ATTRIBUTE20, AbsenceAgreementDEO.ATTRIBUTE21, AbsenceAgreementDEO.ATTRIBUTE22, 
AbsenceAgreementDEO.ATTRIBUTE23, AbsenceAgreementDEO.ATTRIBUTE24, AbsenceAgreementDEO.ATTRIBUTE25, AbsenceAgreementDEO.ATTRIBUTE26, AbsenceAgreementDEO.ATTRIBUTE27, 
AbsenceAgreementDEO.ATTRIBUTE28, AbsenceAgreementDEO.ATTRIBUTE29, AbsenceAgreementDEO.ATTRIBUTE30, AbsenceAgreementDEO.INFORMATION_NUMBER2, 
AbsenceAgreementDEO.INFORMATION_NUMBER1, AbsenceAgreementDEO.INFORMATION_NUMBER3, AbsenceAgreementDEO.INFORMATION_NUMBER4, AbsenceAgreementDEO.INFORMATION_NUMBER5, 
AbsenceAgreementDEO.INFORMATION_NUMBER6, AbsenceAgreementDEO.INFORMATION_NUMBER7, AbsenceAgreementDEO.INFORMATION_NUMBER8, AbsenceAgreementDEO.INFORMATION_NUMBER9, AbsenceAgreementDEO.INFORMATION_NUMBER10, 
AbsenceAgreementDEO.INFORMATION_NUMBER11, AbsenceAgreementDEO.INFORMATION_NUMBER12, AbsenceAgreementDEO.INFORMATION_NUMBER13, AbsenceAgreementDEO.INFORMATION_NUMBER14, AbsenceAgreementDEO.INFORMATION_NUMBER15, 
AbsenceAgreementDEO.INFORMATION_NUMBER16, AbsenceAgreementDEO.INFORMATION_NUMBER17, AbsenceAgreementDEO.INFORMATION_NUMBER18, AbsenceAgreementDEO.INFORMATION_NUMBER19, AbsenceAgreementDEO.INFORMATION_NUMBER20, 
AbsenceAgreementDEO.INFORMATION_DATE1, AbsenceAgreementDEO.INFORMATION_DATE2, AbsenceAgreementDEO.INFORMATION_DATE3, AbsenceAgreementDEO.INFORMATION_DATE4, AbsenceAgreementDEO.INFORMATION_DATE5, 
AbsenceAgreementDEO.INFORMATION_DATE6, AbsenceAgreementDEO.INFORMATION_DATE7, AbsenceAgreementDEO.INFORMATION_DATE8, AbsenceAgreementDEO.INFORMATION_DATE9, AbsenceAgreementDEO.INFORMATION_DATE10, 
AbsenceAgreementDEO.INFORMATION_DATE11, AbsenceAgreementDEO.INFORMATION_DATE12, AbsenceAgreementDEO.INFORMATION_DATE13, AbsenceAgreementDEO.INFORMATION_DATE14, AbsenceAgreementDEO.INFORMATION_DATE15, 
AbsenceAgreementDEO.ATTRIBUTE_NUMBER1, AbsenceAgreementDEO.ATTRIBUTE_NUMBER2, AbsenceAgreementDEO.ATTRIBUTE_NUMBER3, AbsenceAgreementDEO.ATTRIBUTE_NUMBER4, AbsenceAgreementDEO.ATTRIBUTE_NUMBER5, 
AbsenceAgreementDEO.ATTRIBUTE_NUMBER6, AbsenceAgreementDEO.ATTRIBUTE_NUMBER7, AbsenceAgreementDEO.ATTRIBUTE_NUMBER8, AbsenceAgreementDEO.ATTRIBUTE_NUMBER9, AbsenceAgreementDEO.ATTRIBUTE_NUMBER10, 
AbsenceAgreementDEO.ATTRIBUTE_NUMBER11, AbsenceAgreementDEO.ATTRIBUTE_NUMBER12, AbsenceAgreementDEO.ATTRIBUTE_NUMBER13, AbsenceAgreementDEO.ATTRIBUTE_NUMBER14, AbsenceAgreementDEO.ATTRIBUTE_NUMBER15, 
AbsenceAgreementDEO.ATTRIBUTE_NUMBER16, AbsenceAgreementDEO.ATTRIBUTE_NUMBER17, AbsenceAgreementDEO.ATTRIBUTE_NUMBER18, AbsenceAgreementDEO.ATTRIBUTE_NUMBER19, AbsenceAgreementDEO.ATTRIBUTE_NUMBER20, 
AbsenceAgreementDEO.ATTRIBUTE_DATE1, AbsenceAgreementDEO.ATTRIBUTE_DATE2, AbsenceAgreementDEO.ATTRIBUTE_DATE3, AbsenceAgreementDEO.ATTRIBUTE_DATE4, AbsenceAgreementDEO.ATTRIBUTE_DATE5, AbsenceAgreementDEO.ATTRIBUTE_DATE6, 
AbsenceAgreementDEO.ATTRIBUTE_DATE7, AbsenceAgreementDEO.ATTRIBUTE_DATE8, AbsenceAgreementDEO.ATTRIBUTE_DATE9, AbsenceAgreementDEO.ATTRIBUTE_DATE10, AbsenceAgreementDEO.ATTRIBUTE_DATE11, AbsenceAgreementDEO.ATTRIBUTE_DATE12, 
AbsenceAgreementDEO.ATTRIBUTE_DATE13, AbsenceAgreementDEO.ATTRIBUTE_DATE14, AbsenceAgreementDEO.ATTRIBUTE_DATE15, AbsenceAgreementDEO.BASE_NAME, AbsenceAgreementDEO.EVENT_TYPE_CD 
FROM ANC_ABSENCE_AGREEMENTS_F AbsenceAgreementDEO, ANC_ABSENCE_AGREEMENTS_F_TL AbsenceAgreementTranslationDEO 
WHERE AbsenceAgreementDEO.ABSENCE_AGREEMENT_ID = AbsenceAgreementTranslationDEO.ABSENCE_AGREEMENT_ID AND 
AbsenceAgreementTranslationDEO.LANGUAGE = SYS_CONTEXT(\'USERENV\', \'LANG\') AND 
AbsenceAgreementDEO.EFFECTIVE_START_DATE = AbsenceAgreementTranslationDEO.EFFECTIVE_START_DATE AND 
AbsenceAgreementDEO.EFFECTIVE_END_DATE = AbsenceAgreementTranslationDEO.EFFECTIVE_END_DATE"""


sql2 = 'select a.field1 b.field2 from tablea a, tableb b where a.cat> 1 and b.type!=5'

t = Tokenizer(sql)
print(t.parse())


