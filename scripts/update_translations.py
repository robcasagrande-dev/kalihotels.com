import json
import os

langs = ['es', 'en', 'it', 'fr', 'de']
base_path = '/home/robi/Projects/kalihotels.com/src/i18n'

content = {
    'es': {
        'seo_overview': {
            'title': 'Santa Marta a Simple Vista',
            'p1': 'Santa Marta es una de las joyas de Colombia, ofreciendo una mezcla única de historia colonial, vibrante vida urbana y la imponente naturaleza del Parque Nacional Natural Tayrona. Kali Hotels le ofrece la oportunidad perfecta de experimentar lo mejor de ambos mundos.',
            'p2': 'En el Centro Histórico, Casa de Leda y Casa de Isabella ofrecen un refugio boutique de lujo con spas, piscinas en la azotea y un encanto colonial incomparable, a pasos de los mejores restaurantes y vida nocturna. Para aquellos que buscan una conexión profunda con la naturaleza, Villa María Tayrona es nuestro galardonado eco-lodge situado a las puertas del Parque Tayrona, donde el confort excepcional se encuentra con la exuberante selva tropical y las vistas panorámicas al Mar Caribe.'
        },
        'funnel': {
            'title': 'Su Itinerario Perfecto',
            'desc': 'Recomendamos dividir su estadía: 3 noches en el Centro Histórico para absorber la cultura y la gastronomía, seguidas de 3 noches en Villa María para explorar el Parque Tayrona y relajarse en la selva.'
        },
        'faq': {
            'title': 'Preguntas Frecuentes',
            'home': [
                {'q': '¿Cuáles son los mejores hoteles en Santa Marta?', 'a': 'Los mejores hoteles boutique de lujo en Santa Marta son Casa de Leda y Casa de Isabella en el Centro Histórico, y Villa María Tayrona junto al Parque Nacional Tayrona.'},
                {'q': '¿Dónde alojarse cerca del Parque Nacional Tayrona?', 'a': 'Villa María Tayrona by Kali Hotels es el hotel de lujo #1 ubicado a solo 3 km de la entrada principal del Parque Tayrona, con vistas espectaculares al mar Caribe y a la selva.'}
            ],
            'leda': [
                {'q': '¿Casa de Leda tiene piscina?', 'a': 'Sí, Casa de Leda cuenta con una hermosa piscina en la azotea con un bar, además de un spa romano subterráneo.'},
                {'q': '¿Está Casa de Leda en el centro histórico?', 'a': 'Sí, estamos ubicados en el corazón del Centro Histórico de Santa Marta, a poca distancia del Parque de los Novios.'}
            ],
            'isabella': [
                {'q': '¿Tiene Casa de Isabella piscina?', 'a': 'Casa de Isabella cuenta con una refrescante piscina de inmersión en un hermoso patio colonial, así como piscina privada en habitaciones selectas.'},
                {'q': '¿Se puede ir caminando a restaurantes?', 'a': 'Absolutamente. Estamos a una cuadra de los mejores restaurantes y la vida nocturna de Santa Marta.'}
            ],
            'maria': [
                {'q': '¿A qué distancia está Villa María del Parque Tayrona?', 'a': 'Villa María Tayrona se encuentra a solo 3 kilómetros de la entrada principal (El Zaino) del Parque Nacional Tayrona.'},
                {'q': '¿Hay restaurante en Villa María Tayrona?', 'a': 'Sí, contamos con un excelente restaurante en el lugar para que nuestros huéspedes no tengan que conducir para disfrutar de una cena de primera.'}
            ]
        },
        'location': {
            'title': 'Cómo llegar a nuestros hoteles',
            'subtitle': 'Guía de transporte para Santa Marta y Parque Tayrona',
            'airport': 'Desde el Aeropuerto (SMR) hasta el Centro Histórico',
            'airport_desc': 'El aeropuerto Simón Bolívar (SMR) está a unos 30-40 minutos del centro. Recomendamos reservar un traslado privado con nosotros para una llegada sin complicaciones.',
            'tayrona': 'Desde Santa Marta hasta Villa María Tayrona',
            'tayrona_desc': 'Villa María está a 40 minutos en coche de Santa Marta por la vía a Riohacha (Troncal del Caribe). Podemos organizar un transporte privado o puede tomar el autobús público que se dirige al Parque Tayrona.'
        }
    },
    'en': {
        'seo_overview': {
            'title': 'Santa Marta at a Glance',
            'p1': 'Santa Marta is one of Colombia\'s greatest jewels, offering a unique blend of colonial history, vibrant city life, and the breathtaking nature of Tayrona National Natural Park. Kali Hotels offers you the perfect opportunity to experience the best of both worlds.',
            'p2': 'In the Historic Center, Casa de Leda and Casa de Isabella provide a luxury boutique sanctuary with spas, rooftop pools, and unmatched colonial charm, just steps away from top dining and nightlife. For those seeking a deep connection with nature, Villa Maria Tayrona is our award-winning eco-lodge situated at the gates of Tayrona Park, where exceptional comfort meets the lush rainforest and panoramic views of the Caribbean Sea.'
        },
        'funnel': {
            'title': 'Your Perfect Itinerary',
            'desc': 'We recommend splitting your stay: 3 nights in the Historic Center to absorb the culture and gastronomy, followed by 3 nights at Villa Maria to explore Tayrona Park and unwind in the jungle.'
        },
        'faq': {
            'title': 'Frequently Asked Questions',
            'home': [
                {'q': 'What are the best hotels in Santa Marta?', 'a': 'The top luxury boutique hotels in Santa Marta are Casa de Leda and Casa de Isabella in the Historic Center, and Villa Maria Tayrona near Tayrona National Park.'},
                {'q': 'Where to stay near Tayrona National Park?', 'a': 'Villa Maria Tayrona by Kali Hotels is the premier 5-star eco-lodge located just 3 km from the main entrance of Tayrona National Park, offering ocean views and jungle luxury.'}
            ],
            'leda': [
                {'q': 'Does Casa de Leda have a pool?', 'a': 'Yes, Casa de Leda features a beautiful rooftop pool with a bar, as well as a unique subterranean Roman spa.'},
                {'q': 'Is Casa de Leda in the historic center?', 'a': 'Yes, we are located right in the heart of Santa Marta\'s Historic Center, within walking distance of Parque de los Novios.'}
            ],
            'isabella': [
                {'q': 'Does Casa de Isabella have a pool?', 'a': 'Casa de Isabella features a refreshing plunge pool in a beautiful colonial courtyard, as well as a private pool in select rooms.'},
                {'q': 'Can you walk to restaurants?', 'a': 'Absolutely. We are just one block away from the best restaurants and nightlife in Santa Marta.'}
            ],
            'maria': [
                {'q': 'How far is Villa Maria from Tayrona Park?', 'a': 'Villa Maria Tayrona is located just 3 kilometers from the main entrance (El Zaino) of Tayrona National Park.'},
                {'q': 'Is there a restaurant at Villa Maria Tayrona?', 'a': 'Yes, we have an excellent on-site restaurant so our guests don\'t have to drive to enjoy a world-class dinner.'}
            ]
        },
        'location': {
            'title': 'How to get to our hotels',
            'subtitle': 'Transportation guide for Santa Marta and Tayrona Park',
            'airport': 'From the Airport (SMR) to the Historic Center',
            'airport_desc': 'The Simon Bolivar airport (SMR) is about 30-40 minutes from the center. We recommend booking a private transfer with us for a hassle-free arrival.',
            'tayrona': 'From Santa Marta to Villa Maria Tayrona',
            'tayrona_desc': 'Villa Maria is a 40-minute drive from Santa Marta on the road to Riohacha. We can arrange a private transfer or you can take the public bus heading to Tayrona Park.'
        }
    }
}

for lang in ['it', 'fr', 'de']:
    content[lang] = content['en']

for lang in langs:
    filepath = os.path.join(base_path, f'{lang}.json')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        data['seo_overview'] = content[lang]['seo_overview']
        data['funnel'] = content[lang]['funnel']
        data['faq'] = content[lang]['faq']
        data['location'] = content[lang]['location']
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print("Translations updated successfully.")
