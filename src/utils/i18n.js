import es from '../i18n/es.json';
import en from '../i18n/en.json';
import it from '../i18n/it.json';

const translations = { es, en, it };

export const LANGUAGES = ['es', 'en', 'it'];
export const DEFAULT_LANGUAGE = 'es';

export function getTranslations(lang) {
  return translations[lang] || translations[DEFAULT_LANGUAGE];
}
