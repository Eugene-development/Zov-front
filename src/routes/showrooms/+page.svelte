<script>
	import { onMount } from 'svelte';
	import Modal from '$lib/components/Modal.svelte';
	import DesignerForm from '$lib/components/DesignerForm.svelte';
	import ShowroomForm from '$lib/components/ShowroomForm.svelte';
	import { regionState } from '$lib/state/region.svelte';

	let heroVisible = $state(false);
	let isDesignerModalOpen = $state(false);
	let isShowroomModalOpen = $state(false);
	let sections = $state({});
	let mapContainer = $state(null);
	let mapInstance = $state(null);
	let searchQuery = $state('');

	onMount(() => {
		heroVisible = true;

		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						sections[entry.target.id] = true;
					}
				});
			},
			{ threshold: 0.15, rootMargin: '0px 0px -50px 0px' }
		);

		// Initialize Map
		function initMap() {
			if (!mapContainer || typeof window.ymaps === 'undefined') return;
			mapInstance = new window.ymaps.Map(mapContainer, {
				center: [54.5, 31.0],
				zoom: 5,
				controls: ['zoomControl', 'fullscreenControl']
			});
		}

		if (window.ymaps) {
			window.ymaps.ready(initMap);
		} else {
			let script = document.querySelector('script[src*="api-maps.yandex.ru"]');
			if (!script) {
				script = document.createElement('script');
				script.src = 'https://api-maps.yandex.ru/2.1/?lang=ru_RU';
				document.head.appendChild(script);
			}
			script.addEventListener('load', () => {
				window.ymaps.ready(initMap);
			});
		}

		document.querySelectorAll('[data-animate]').forEach((el) => {
			observer.observe(el);
		});

		return () => {
			observer.disconnect();
			if (mapInstance) {
				mapInstance.destroy();
			}
		};
	});

	const showrooms = {
		Беларусь: [
			{
				city: 'Гродно',
				places: [
					{
						name: 'Флагманский салон ЗОВ',
						address: 'ул. Индустриальная, 9',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [53.649, 23.823]
					}
				]
			},
			{
				city: 'Минск',
				places: [
					{
						name: 'ТЦ «Замок Home»',
						address: 'пр-т Победителей, 65, 4 этаж',
						hours: 'Пн-Вс: 10:00 – 22:00',
						coords: [53.926, 27.518]
					},
					{
						name: 'ТЦ «Камелот»',
						address: 'ул. Мазурова, 1',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [53.890632, 27.433431]
					}
				]
			}
		],
		Россия: [
			{
				city: 'Москва и МО',
				places: [
					// ,
					// {
					// 	address: '',
					// 	hours: 'Пн-Вс: 10:00 – 20:00',
					// 	coords: []
					// },
					{
						address: 'г. Москва, Подольское ш., д. 8, корп. 5',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [55.709324, 37.653457]
					},
					{
						address: 'г. Москва, Ленинградский пр-т, д. 74, корп. 1',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [55.805133, 37.516952]
					},
					{
						address: 'г. Москва, Тихорецкий б-р, д. 1, корп. 5, ТЦ «ЛЮБЛИНСКОЕ ПОЛЕ»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [55.678, 37.7712]
					},
					{
						address: 'г. Москва, Варшавское ш., д. 94',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [55.6385, 37.6208]
					},
					{
						address: 'г. Москва, ул. Ярцевская, д. 19, МФК «Кунцево Плаза»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [55.7394, 37.4093]
					},
					{
						address: 'г. Москва, Рязанский пр-т, д. 2, корп. 2, ТРЦ «Город»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [55.732, 37.753]
					},
					{
						address: 'г. Москва, Локомотивный проезд, д. 4, ТЦ «Парус»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [55.845, 37.574]
					},
					{
						address: 'г. Москва, ул. Вавилова, д. 3, ТРЦ «ГАГАРИНСКИЙ»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [55.707, 37.592]
					},
					{
						address: 'г. Москва, МКАД, 25-й км, вл. 1, ТЦ «Конструктор», 2 этаж',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ш. Энтузиастов, д. 76/1',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Дмитровское ш., д. 73, корп. 1, ТЦ «Metromall»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, пр-т Мира, д. 33, корп. 1, торгово-офисный центр «OLYMPIC PLAZA»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Комсомольский пр-т, д. 19',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ул. Таганская, д. 3, ТЦ «Таганский Пассаж»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ул. Ленинская Слобода, д. 26, МЦ «ROOMER»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Волоколамское ш., д. 71/22 , корп. 3',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Хорошёвское ш., д. 16, стр. 3, ТЦ «На Беговой»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Ленинградское ш., д. 25, МЦ «FAMILY ROOM»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, пр-т Мира, д. 211, корп. 2, ТРК «ЕВРОПОЛИС»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Ходынский бульвар, д. 4, ТЦ «АВИАПАРК»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Варшавское ш., д. 160, ТРЦ «ГАЛЕРЕЯ АТЛАНТИС»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, МКАД, 71-й км, стр. 16, ТЦ «КухниПарк»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Коровинское ш., д. 2, ТРЦ «Avenue sever», -1 этаж',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ул. Кировоградская, д. 15, МТЦ «Гранд Юг»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Красногорск, ул. Международная, д. 4, гипермаркет «Твой Дом»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Реутов, МКАД, 2-й км, д. 2, ТК «Шоколад»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, наб. Тараса Шевченко, д. 1',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Одинцово, ул. Вокзальная, д. 2, ТЦ «Андромеда»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'р.п. Новоивановское, ул. Луговая, д. 1, МЦ «Три Кита»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Чехов, ул. Московская, д. 83',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Дмитровское ш., д. 161Б, МЦ «Империя»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Дмитровское ш., д. 161Б, МЦ «Империя»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Дмитровское ш., д. 163А, корп. 1, ТРЦ «РИО»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Королёв, ул. Лермонтова, д. 10, корп. 3',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ул. Пришвина, д. 26, ТВК «Миллион мелочей»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Московский, 1-й мкр., д. 58, Cпортивно-развлекательный центр «НЕБО АРЕНА»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ул. Дубравная, д. 51, стр. 1, ТРЦ «Митино Парк»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Химки, ул. Молодёжная, д. 78',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ул. Полярная, д. 21, ТЦ «Дом Мебели»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Красногорск, Новорижское ш., 23-й км, вл. 2, стр. 1, ТРЦ «РИГАМОЛЛ»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ул. Зорге, д. 1, стр. 2, ТЦ «Дом для Дома»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Новоухтомское ш., д. 2А, ТРЦ «Город Косино»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г.о. Красногорск, пос. Отрадное, Пятницкое ш., д. 1, стр. 1, ТП «Отрада»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Мичуринский пр-т, д. 10, корп. 1',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Можайское ш., д. 25',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Мытищи, ул. Мира, д. 39',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ул. Люблинская, д. 165',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Химки, ул. Бутаково, д. 4, МЦ «Гранд»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ш. Энтузиастов, д. 12, корп. 2, ТРЦ «ГОРОД Лефортово»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Волгоградский пр-т, д. 132',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Домодедово, Каширское ш., д. 17Г, МЦ «ДОМ», «Торговая галерея»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address:
							'г. Москва, Киевское ш., 22-ой км, д. 4, стр. 2, корп. В, ТЦ «Мебель Park», БП «Румянцево», вход 5, 3 этаж, пав. 327В',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Реутов, Юбилейный пр-т, д. 47',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Балашиха, ул. Юбилейная, д. 4, корп. 5',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Жуковский, ул. Королёва, д. 6, стр. 3',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Ногинск, ул. Трудовая, д. 4Б, ТД «Люкс»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, пр-т Маршала Жукова, д. 59',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Балашиха, ул. Свердлова, д. 7',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Красногорск, ул. Ленина, д. 2, ТЦ «Красный Кит»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, МКАД, 84-й км, вл. 3, стр. 1, ТЦ «Ашан»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ул. А. Монаховой, д. 109, корп. 1',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Боровское ш., д. 20',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Балашиха, пр-т Ленина, д. 8',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Люберцы, Октябрьский пр-т, д. 112, ТРЦ «ВЫХОДНОЙ»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Орехово-Зуево, ул. Урицкого, д. 92, ТЦ «БАРРИКАДА»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Дмитровское ш., д. 124А',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ул. Обручева, д. 34/63, стр.1, ТЦ «Мебель BOX»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, 7-я Кожуховская ул., д. 9, ТРЦ «Мозаика»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Раменское, ул. 1-ая Ленинская, д. 37, гипермаркет мебели «МЕБЕЛЬdom»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ул. Бутырская, д. 65/68',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Мытищи, ул. Коммунистическая, д. 10, корп. 1, ТЦ «XL HOME»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Каширское ш., д. 62/2',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ул. Шереметьевская, д. 20, ТЦ «Капитолий»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Мытищи, Осташковское ш., д. 2, ТЦ «Твой дом»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, пр-т Вернадского, д. 86А, ТРЦ «AVENUE»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, ул. Рябиновая, д. 41, корп. 1, ДЦ «MADEX»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Люберцы, Новорязанское ш., д. 3, ТК «ГРАНТ»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Пушкино, Красноармейское ш., д. 101, стр. 2',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Москва, Сиреневый бульвар, д. 31, ТЦ «София»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: 'г. Воскресенск, ул. Зелинского, д. 2, ТЦ «Вега»',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address:
							'г. Воскресенск, ул. Лопатинская, д. 11А, строительный рынок «Планета», пав. 30',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: '',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: '',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: '',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: '',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: '',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: '',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: '',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: '',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: '',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: '',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					},
					{
						address: '',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: []
					}
				]
			},
			{
				city: 'Санкт-Петербург',
				places: [
					{
						name: 'ТЦ «Мебельный Континент»',
						address: 'ул. Варшавская, 3',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [59.882, 30.312]
					}
				]
			}
		]
	};

	let filteredShowrooms = $derived.by(() => {
		for (const [country, cities] of Object.entries(showrooms)) {
			const cityData = cities.filter((c) => c.city === regionState.selectedCity);
			if (cityData.length > 0) {
				const clonedCityData = cityData.map((c) => {
					const filteredPlaces = c.places.filter((p) => {
						if (!searchQuery) return true;
						const query = searchQuery.toLowerCase();
						const matchName = p.name && p.name.toLowerCase().includes(query);
						const matchAddress = p.address && p.address.toLowerCase().includes(query);
						return matchName || matchAddress;
					});
					return { ...c, places: filteredPlaces };
				});
				return clonedCityData.filter((c) => c.places.length > 0);
			}
		}
		return [];
	});

	let totalPlaces = $derived(filteredShowrooms.reduce((acc, curr) => acc + curr.places.length, 0));

	$effect(() => {
		if (!mapInstance || typeof window.ymaps === 'undefined') return;

		mapInstance.geoObjects.removeAll();

		const CustomPin =
			'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAiIGhlaWdodD0iNDgiIHZpZXdCb3g9IjAgMCA0MCA0OCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMjAgMEM4Ljk1NCAwIDAgOC45NTQgMCAyMGMwIDE0LjQgMjAgMjggMjAgMjhzMjAtMTMuNiAyMC0yOGMwLTExLjA0Ni04Ljk1NC0yMC0yMC0yMFoiIGZpbGw9IiM4YjczNTUiLz48Y2lyY2xlIGN4PSIyMCIgY3k9IjIwIiByPSI4IiBmaWxsPSJ3aGl0ZSIvPjwvc3ZnPg==';

		filteredShowrooms.forEach((city) => {
			city.places.forEach((place) => {
				if (place.coords && place.coords.length === 2) {
					const placemark = new window.ymaps.Placemark(
						place.coords,
						{
							balloonContentHeader: place.name || 'Салон ЗОВ',
							balloonContentBody: place.address,
							balloonContentFooter: place.hours
						},
						{
							preset: 'islands#brownIcon',
							hideIconOnBalloonOpen: false,
							balloonOffset: [0, -30]
						}
					);
					mapInstance.geoObjects.add(placemark);
				}
			});
		});

		const bounds = mapInstance.geoObjects.getBounds();
		if (bounds) {
			mapInstance
				.setBounds(bounds, {
					checkZoomRange: true,
					zoomMargin: 50,
					duration: 400
				})
				.then(() => {
					if (mapInstance.getZoom() > 15) {
						mapInstance.setZoom(15);
					}
				});
		} else {
			mapInstance.setCenter([54.5, 31.0], 5);
		}
	});
</script>

<svelte:head>
	<title>Салоны ЗОВ | Адреса в России и Беларуси</title>
	<meta
		name="description"
		content="Найдите ближайший фирменный салон мебели ЗОВ в вашем городе. Более 120 салонов в России и Беларуси. Адреса, контакты, время работы и интерактивная карта."
	/>
</svelte:head>

<!-- ==================== HERO SECTION ==================== -->
<section class="relative min-h-[90vh] overflow-hidden bg-surface" id="hero">
	<!-- Background Image -->
	<div class="absolute inset-0">
		<img
			src="/images/modern_showroom.png"
			alt="Интерьер салона ЗОВ"
			class="h-full w-full object-cover transition-transform duration-[2s]"
			class:scale-105={heroVisible}
		/>
		<div
			class="absolute inset-0 bg-gradient-to-r from-primary/90 via-primary/60 to-transparent"
		></div>
	</div>

	<!-- Content -->
	<div class="relative z-10 flex min-h-[90vh] items-center">
		<div class="mx-auto w-full max-w-7xl px-6">
			<div class="max-w-xl">
				<div
					class="mb-6 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.3s"
				>
					<span class="text-[11px] tracking-[0.3em] text-white/70 uppercase">Где купить</span>
				</div>
				<h1
					class="text-5xl leading-[1.1] font-light text-white opacity-0 md:text-6xl lg:text-7xl"
					style="font-family: var(--font-heading); animation-delay: 0.5s"
					class:animate-fade-up={heroVisible}
				>
					Наши <span class="text-accent-light">салоны</span>
				</h1>
				<p
					class="mt-6 text-base leading-relaxed text-white/70 opacity-0 md:text-lg"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.7s"
				>
					Посетите один из наших фирменных салонов. Оцените качество материалов вживую, вдохновитесь
					готовыми интерьерными решениями и создайте проект вашей кухни вместе с профессиональными
					дизайнерами.
				</p>
				<div
					class="mt-10 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.9s"
				>
					<a
						href="#network-section"
						class="group inline-flex cursor-pointer items-center gap-3 rounded-sm border border-secondary bg-secondary px-8 py-4 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:bg-transparent"
					>
						Посмотреть карту
						<svg
							class="h-4 w-4 transition-transform duration-300 group-hover:translate-y-1"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
							stroke-width="1.5"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M19.5 13.5 12 21m0 0-7.5-7.5M12 21V3"
							/>
						</svg>
					</a>
				</div>
			</div>
		</div>
	</div>

	<!-- Scroll Indicator -->
	<div
		class="absolute bottom-10 left-1/2 -translate-x-1/2 opacity-0"
		class:animate-fade-in={heroVisible}
		style="animation-delay: 1.3s"
	>
		<div class="flex flex-col items-center gap-2">
			<span class="text-[10px] tracking-[0.3em] text-white/50 uppercase">Вниз</span>
			<div class="h-10 w-px bg-gradient-to-b from-white/50 to-transparent"></div>
		</div>
	</div>
</section>

<!-- ==================== MAP & LIST SECTION ==================== -->
<section
	class="relative scroll-mt-20 bg-surface py-section lg:scroll-mt-24"
	id="network-section"
	data-animate
>
	<div class="mx-auto max-w-7xl px-6">
		<div class="grid items-start gap-16 lg:grid-cols-12 lg:gap-12">
			<!-- Left Column: Locations List -->
			<div
				class="flex flex-col opacity-0 lg:col-span-5"
				class:animate-fade-up={sections['network-section']}
			>
				<h2
					class="text-3xl font-light text-primary lg:text-4xl"
					style="font-family: var(--font-heading);"
				>
					Дилерская сеть салонов в Беларуси и России
				</h2>

				<div
					class="mt-8 flex flex-col items-start gap-4 border-b border-border-light pb-6 sm:flex-row sm:items-center"
				>
					<button
						class="group inline-flex h-12 shrink-0 cursor-pointer items-center gap-3 rounded-sm border border-border-medium px-5 text-xs tracking-[0.1em] text-primary transition-all duration-300 hover:border-secondary hover:text-secondary"
						onclick={() => (regionState.isCityModalOpen = true)}
					>
						Ваш город: <span class="font-medium text-secondary">{regionState.selectedCity}</span>
						<svg
							class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
							stroke-width="1.5"
						>
							<path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
						</svg>
					</button>

					<div class="relative w-full max-w-sm">
						<div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
							<svg
								class="h-4 w-4 text-muted"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								stroke-width="1.5"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
								/>
							</svg>
						</div>
						<input
							type="text"
							bind:value={searchQuery}
							placeholder="Поиск по адресу..."
							class="h-12 w-full rounded-sm border border-border-medium bg-transparent pr-4 pl-10 text-sm text-primary transition-all duration-300 placeholder:text-muted focus:border-secondary focus:ring-0 focus:outline-none"
						/>
					</div>
				</div>

				<!-- Cities List -->
				<div class="relative -mx-2 mt-8 px-2">
					<div
						class="flex flex-col gap-10 {totalPlaces > 3
							? 'max-h-[400px] overflow-y-auto pr-4 pb-10 [&::-webkit-scrollbar]:w-1.5 [&::-webkit-scrollbar-thumb]:rounded-full [&::-webkit-scrollbar-thumb]:bg-border-light/80 hover:[&::-webkit-scrollbar-thumb]:bg-border-light [&::-webkit-scrollbar-track]:bg-transparent'
							: ''}"
					>
						{#each filteredShowrooms as data (data.city)}
							<div>
								<h3
									class="flex items-center gap-3 text-xl font-medium text-primary"
									style="font-family: var(--font-heading);"
								>
									<svg
										class="h-5 w-5 text-secondary"
										fill="none"
										viewBox="0 0 24 24"
										stroke="currentColor"
										stroke-width="1.5"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"
										/>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"
										/>
									</svg>
									{data.city}
								</h3>

								<div class="mt-6 flex flex-col gap-6">
									{#each data.places as place, i ((place.name ?? place.address) + i)}
										<div
											class="group border-l-2 border-border-light pl-6 transition-colors duration-300 hover:border-secondary"
										>
											{#if place.name}
												<h4 class="text-base font-medium text-primary">{place.name}</h4>
											{/if}
											<p class="{place.name ? 'mt-2' : ''} text-sm text-secondary">
												{place.address}
											</p>
											<div class="mt-4 flex flex-col gap-1.5 text-xs text-muted">
												<div class="flex items-center gap-2">
													<svg
														class="h-3.5 w-3.5"
														fill="none"
														viewBox="0 0 24 24"
														stroke="currentColor"
														stroke-width="1.5"
													>
														<path
															stroke-linecap="round"
															stroke-linejoin="round"
															d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"
														/>
													</svg>
													{place.hours}
												</div>
											</div>
										</div>
									{/each}
								</div>
							</div>
						{/each}

						{#if filteredShowrooms.length === 0}
							<div class="flex flex-col items-center py-12 text-center">
								<svg
									class="h-10 w-10 text-border-medium"
									fill="none"
									viewBox="0 0 24 24"
									stroke="currentColor"
									stroke-width="1.5"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"
									/>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"
									/>
								</svg>
								<p class="mt-4 text-sm text-secondary">
									В выбранном городе пока нет наших фирменных салонов.
								</p>
								<p class="mt-2 text-xs text-muted">Вы можете оформить заявку на выездной расчет.</p>
							</div>
						{/if}
					</div>
					{#if totalPlaces > 3}
						<div
							class="pointer-events-none absolute bottom-0 left-0 h-24 w-full bg-gradient-to-t from-surface to-transparent"
						></div>
					{/if}
				</div>

				<div class="mt-10 flex">
					<button
						onclick={() => (isShowroomModalOpen = true)}
						class="group inline-flex cursor-pointer items-center gap-3 rounded-sm border border-border-medium px-6 py-3 text-xs tracking-[0.15em] text-primary uppercase transition-all duration-500 hover:border-secondary hover:text-secondary"
					>
						Запись в салон
						<svg
							class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
							stroke-width="1.5"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
							/>
						</svg>
					</button>
				</div>
			</div>

			<!-- Right Column: Yandex Interactive Map -->
			<div
				class="sticky top-32 h-[600px] opacity-0 lg:col-span-7 lg:h-[750px]"
				class:animate-fade-up={sections['network-section']}
				style="animation-delay: 0.3s"
			>
				<div class="relative h-full w-full overflow-hidden bg-surface-warm shadow-soft">
					<div
						bind:this={mapContainer}
						class="absolute inset-0 [filter:sepia(0.3)_saturate(0.5)_contrast(1.05)_brightness(0.98)] transition-all duration-1000 hover:[filter:none]"
					></div>
				</div>
			</div>
		</div>
	</div>
</section>

<!-- ==================== CTA SECTION ==================== -->
<section
	class="relative overflow-hidden bg-primary py-section-sm lg:py-section"
	id="cta-section"
	data-animate
>
	<div
		class="absolute inset-0 opacity-[0.03]"
		style="background-image: url('data:image/svg+xml,%3Csvg width=\'60\' height=\'60\' viewBox=\'0 0 60 60\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cg fill=\'none\' fill-rule=\'evenodd\'%3E%3Cg fill=\'%23ffffff\'%3E%3Cpath d=\'M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');"
	></div>

	<div class="relative mx-auto max-w-4xl px-6 text-center">
		<div class="opacity-0" class:animate-fade-up={sections['cta-section']}>
			<h2
				class="text-3xl font-light text-white lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Нет времени на поездку в салон?
			</h2>
			<p class="mx-auto mt-6 max-w-2xl text-base leading-relaxed text-white/70">
				Закажите выезд дизайнера на дом абсолютно бесплатно. Наш специалист приедет с образцами
				фасадов и столешниц, снимет точные замеры и создаст 3D-проект вашей будущей кухни прямо на
				месте.
			</p>

			<div class="mt-10 flex flex-wrap items-center justify-center gap-4">
				<button
					onclick={() => (isDesignerModalOpen = true)}
					class="group inline-flex cursor-pointer items-center gap-3 rounded-sm border border-secondary bg-secondary px-8 py-4 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:bg-transparent hover:text-secondary"
				>
					Вызвать дизайнера
					<svg
						class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
						stroke-width="1.5"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
						/>
					</svg>
				</button>
			</div>
		</div>
	</div>
</section>

<!-- Modals -->
<Modal bind:showModal={isDesignerModalOpen} title="Вызов дизайнера">
	<DesignerForm onSuccess={() => (isDesignerModalOpen = false)} />
</Modal>

<Modal bind:showModal={isShowroomModalOpen} title="Запись в салон">
	<ShowroomForm onSuccess={() => (isShowroomModalOpen = false)} />
</Modal>
