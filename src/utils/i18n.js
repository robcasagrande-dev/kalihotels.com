import es from '../i18n/es.json';
import en from '../i18n/en.json';
import it from '../i18n/it.json';
import fr from '../i18n/fr.json';
import de from '../i18n/de.json';

const translations = { es, en, it, fr, de };

export const LANGUAGES = ['es', 'en', 'it', 'fr', 'de'];
export const DEFAULT_LANGUAGE = 'es';

export function getTranslations(lang) {
  return translations[lang] || translations[DEFAULT_LANGUAGE];
}
