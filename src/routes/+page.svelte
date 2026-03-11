<script>
	import { onMount } from 'svelte';
	import Modal from '$lib/components/Modal.svelte';
	import DesignerForm from '$lib/components/DesignerForm.svelte';

	let heroVisible = $state(false);
	let isDesignerModalOpen = $state(false);
	let sections = $state({});

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

		document.querySelectorAll('[data-animate]').forEach((el) => {
			observer.observe(el);
		});

		return () => observer.disconnect();
	});

	const styles = [
		{
			title: 'Современный',
			description: 'Чистые линии, минималистичные формы и функциональность мебели',
			image: '/images/style-modern.png'
		},
		{
			title: 'Классический',
			description: 'Элегантность мебельных традиций с вниманием к каждой детали фасада',
			image: '/images/style-classic.png'
		},
		{
			title: 'Минимализм',
			description: 'Совершенство в простоте кухрнного гарнитура, пространство и свет',
			image: '/images/style-minimalist.png'
		}
	];

	const advantages = [
		{
			number: '01',
			title: 'Собственное производство',
			description:
				'Полный цикл производства на современном оборудовании ведущих европейских брендов'
		},
		{
			number: '02',
			title: 'Премиальные материалы',
			description: 'Только сертифицированные материалы и комплектующие от мировых лидеров отрасли'
		},
		{
			number: '03',
			title: 'Индивидуальный дизайн',
			description: 'Каждый проект создаётся по вашим размерам с учётом всех пожеланий клиента'
		},
		{
			number: '04',
			title: 'Гарантия качества',
			description:
				'Многоступенчатый фабричный контроль качества и гарантия до 5 лет на всю продукцию'
		}
	];

	const stats = [
		{ value: '25+', label: 'лет опыта' },
		{ value: '50 000+', label: 'реализованных проектов' },
		{ value: '120+', label: 'салонов по всей стране' },
		{ value: '500+', label: 'оттенков фасадов' }
	];
</script>

<svelte:head>
	<title>ЗОВ — Мебельная фабрика | Кухни и мебель премиум-класса</title>
	<meta
		name="description"
		content="Фабрика ЗОВ — производитель кухонь и мебели премиального качества. Более 20 лет создаём пространства, о которых вы мечтаете."
	/>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link
		href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<!-- ==================== HERO SECTION ==================== -->
<section class="relative min-h-[90vh] overflow-hidden bg-surface" id="hero">
	<!-- Background Image with Overlay -->
	<div class="absolute inset-0">
		<img
			src="/images/hero-kitchen.png"
			alt="Премиальная кухня ЗОВ"
			class="h-full w-full object-cover transition-transform duration-[2s]"
			class:scale-105={heroVisible}
		/>
		<div class="absolute inset-0 bg-gradient-to-r from-white/85 via-white/50 to-transparent"></div>
		<div class="absolute inset-0 bg-gradient-to-t from-white/40 to-transparent"></div>
	</div>

	<!-- Content -->
	<div class="relative z-10 flex min-h-[85vh] items-center">
		<div class="mx-auto w-full max-w-7xl px-6">
			<div class="max-w-2xl">
				<!-- Label -->
				<div
					class="mb-6 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.3s"
				>
					<span
						class="inline-flex items-center gap-2 border border-secondary/30 bg-white/60 px-4 py-2 text-[11px] tracking-[0.25em] text-secondary uppercase backdrop-blur-sm"
					>
						<!-- <span class="h-1.5 w-1.5 rounded-full bg-secondary"></span> -->
						Белорусская фабрика мебели
					</span>
				</div>

				<!-- Heading -->
				<h1
					class="text-5xl leading-[1.1] font-light text-primary opacity-0 md:text-6xl lg:text-7xl"
					style="font-family: var(--font-heading); animation-delay: 0.5s"
					class:animate-fade-up={heroVisible}
				>
					Пространства,
					<br />
					в которых
					<br class="md:hidden" />
					<span class="font-normal text-secondary">живёт стиль</span>
				</h1>

				<!-- Description -->
				<p
					class="mt-8 max-w-md text-base leading-relaxed text-primary opacity-0 md:text-lg"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.7s"
				>
					Создаём кухни и мебель, которые сочетают безупречный дизайн, премиальные материалы и
					выверенную функциональность
				</p>

				<!-- CTA Buttons -->
				<div
					class="mt-10 flex flex-wrap items-center gap-4 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.9s"
				>
					<button
						onclick={() => (isDesignerModalOpen = true)}
						class="group inline-flex items-center gap-3 border border-primary bg-primary px-8 py-4 text-xs tracking-[0.15em] text-text-inverse uppercase transition-all duration-500 hover:border-secondary hover:bg-secondary"
					>
						Дизайнер на дом
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
					<a
						href="/about"
						class="group inline-flex items-center gap-3 border border-border-medium bg-white/60 px-8 py-4 text-xs tracking-[0.15em] text-primary uppercase backdrop-blur-sm transition-all duration-500 hover:border-secondary hover:text-secondary"
					>
						О фабрике
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
			<span class="text-[10px] tracking-[0.3em] text-text-muted uppercase">Листайте</span>
			<div class="h-10 w-px bg-gradient-to-b from-text-muted to-transparent"></div>
		</div>
	</div>
</section>

<!-- ==================== LEADER SECTION ==================== -->
<section
	class="relative z-10 overflow-hidden bg-surface py-20 lg:py-32"
	id="leader-section"
	data-animate
>
	<!-- Decorative Background Lines -->
	<div
		class="absolute top-0 left-0 h-px w-full bg-gradient-to-r from-transparent via-border-light to-transparent"
	></div>
	<div
		class="absolute bottom-0 left-0 h-px w-full bg-gradient-to-r from-transparent via-border-light to-transparent"
	></div>

	<!-- Subtle Background Pattern -->
	<div
		class="pointer-events-none absolute inset-0 opacity-[0.02]"
		style="background-image: url('data:image/svg+xml,%3Csvg width=\'60\' height=\'60\' viewBox=\'0 0 60 60\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cg fill=\'none\' fill-rule=\'evenodd\'%3E%3Cg fill=\'%232c2c2c\'%3E%3Cpath d=\'M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');"
	></div>

	<!-- Abstract shape -->
	<div
		class="absolute -top-32 -right-32 h-96 w-96 rounded-full border border-accent/10 lg:h-[36rem] lg:w-[36rem]"
	></div>

	<div class="relative mx-auto max-w-7xl px-6">
		<div class="flex flex-col items-center justify-between gap-16 lg:flex-row lg:gap-24">
			<!-- Logo -->
			<div
				class="relative flex w-full justify-center opacity-0 lg:w-5/12 lg:justify-end"
				class:animate-fade-up={sections['leader-section']}
				style="animation-delay: 0.2s"
			>
				<div class="relative">
					<!-- Glow effect -->
					<div
						class="absolute inset-0 -m-8 scale-110 rounded-full bg-primary/[0.03] blur-3xl"
					></div>
					<!-- Frame accents -->
					<div
						class="absolute -top-6 -left-6 h-12 w-12 border-t border-l border-accent/40 transition-transform duration-700 hover:-translate-x-2 hover:-translate-y-2 lg:h-16 lg:w-16"
					></div>
					<div
						class="absolute -right-6 -bottom-6 h-12 w-12 border-r border-b border-accent/40 transition-transform duration-700 hover:translate-x-2 hover:translate-y-2 lg:h-16 lg:w-16"
					></div>
					<img
						src="https://storage.yandexcloud.net/zovrus/brand/logo-white.svg"
						alt="Логотип фабрики ЗОВ"
						class="relative z-10 w-64 object-contain opacity-80 invert transition-transform duration-1000 hover:scale-105 hover:opacity-100 md:w-80 lg:w-[26rem]"
					/>
				</div>
			</div>

			<!-- Text Content -->
			<div
				class="relative flex w-full flex-col items-center text-center opacity-0 lg:w-7/12 lg:items-start lg:text-left"
				class:animate-fade-up={sections['leader-section']}
				style="animation-delay: 0.4s"
			>
				<!-- Large Quote Icon -->
				<svg
					class="absolute -top-10 -left-6 -z-10 h-28 w-28 text-primary/[0.03] md:-left-12 lg:-top-16 lg:-left-20 lg:h-48 lg:w-48"
					fill="currentColor"
					viewBox="0 0 24 24"
				>
					<path
						d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"
					/>
				</svg>

				<h2
					class="text-3xl font-light text-primary md:text-4xl lg:text-[2.5rem] lg:leading-tight"
					style="font-family: var(--font-heading);"
				>
					<span class="text-secondary italic">«Мебель для жизни»</span>
				</h2>

				<div class="mt-8 space-y-4">
					<p class="text-base leading-relaxed text-text-secondary">
						Мы вкладываем весь свой опыт и душу в создание мебели, чтобы она приносила уют и комфорт
						в ваш дом на долгие годы.
					</p>
					<p class="text-base leading-relaxed text-text-secondary">
						Каждая кухня, гардероб и любая другая мебель — это результат кропотливого труда нашей
						команды, где передовые технологии сочетаются с подлинной любовью к своему делу.
					</p>
					<p class="text-base leading-relaxed text-text-secondary">
						Мы гордимся тем, что можем стать частью вашей повседневной жизни.
					</p>
				</div>

				<div
					class="mt-10 flex w-full flex-col items-center border-t border-border-light pt-8 lg:flex-row lg:items-center lg:justify-between lg:border-t-0 lg:border-l lg:pt-0 lg:pl-8"
				>
					<div class="flex flex-col items-center lg:items-start">
						<p class="mt-1.5 text-sm font-medium tracking-[0.1em] text-primary">Зуховицкий О.В.</p>
						<p class="mt-1 text-[11px] tracking-wider text-text-muted uppercase">
							Руководитель мебельной фабрики «ЗОВ»
						</p>
					</div>
					<!-- Decorative Stamp/Sign -->
					<div
						class="mt-6 flex h-14 w-14 items-center justify-center rounded-full border border-primary/10 text-primary/20 opacity-60 lg:mt-0"
					>
						<svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="1.5"
								d="M15.362 5.214A8.252 8.252 0 0112 21 8.25 8.25 0 016.038 7.048 8.287 8.287 0 009 9.6a8.983 8.983 0 013.361-6.867 8.21 8.21 0 003 2.48z"
							/>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="1.5"
								d="M12 18a3.75 3.75 0 00.495-7.467 5.99 5.99 0 00-1.925 3.546 5.974 5.974 0 01-2.133-1A3.75 3.75 0 0012 18z"
							/>
						</svg>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<!-- ==================== STYLES SECTION ==================== -->
<section class="relative z-10 mt-16 px-6 lg:mt-24" id="styles-section" data-animate>
	<div class="mx-auto max-w-7xl">
		<!-- Section Header -->
		<div class="mb-12 flex flex-col items-start justify-between gap-6 md:flex-row md:items-end">
			<div
				class="opacity-0 transition-all duration-700"
				class:animate-fade-up={sections['styles-section']}
			>
				<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Коллекции</span>
				<h2
					class="mt-3 text-4xl font-light text-primary lg:text-5xl"
					style="font-family: var(--font-heading);"
				>
					Найдите свой стиль
				</h2>
			</div>
			<a
				href="/styles"
				class="group flex items-center gap-2 text-sm text-text-secondary transition-colors duration-300 hover:text-secondary"
			>
				Все стили
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
			</a>
		</div>

		<!-- Styles Grid -->
		<div class="grid gap-6 md:grid-cols-3">
			{#each styles as style, i}
				<a
					href="/styles"
					class="group relative overflow-hidden bg-white shadow-card transition-all duration-500 hover:-translate-y-1 hover:shadow-elevated"
					style="animation-delay: {0.2 + i * 0.15}s"
				>
					<!-- Image -->
					<div class="relative aspect-[4/5] overflow-hidden">
						<img
							src={style.image}
							alt={style.title}
							class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
						/>
						<div
							class="absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent opacity-0 transition-opacity duration-500 group-hover:opacity-100"
						></div>
					</div>

					<!-- Content -->
					<div class="p-6 lg:p-8">
						<h3
							class="text-2xl font-light text-primary lg:text-3xl"
							style="font-family: var(--font-heading);"
						>
							{style.title}
						</h3>
						<p class="mt-2 text-sm leading-relaxed text-text-secondary">
							{style.description}
						</p>
						<div
							class="mt-4 flex items-center gap-2 text-xs tracking-wider text-secondary opacity-0 transition-all duration-500 group-hover:opacity-100"
						>
							Подробнее
							<svg
								class="h-3.5 w-3.5 transition-transform duration-300 group-hover:translate-x-1"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								stroke-width="2"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
								/>
							</svg>
						</div>
					</div>
				</a>
			{/each}
		</div>
	</div>
</section>

<!-- ==================== ADVANTAGES SECTION ==================== -->
<section
	class="relative overflow-hidden py-section-sm lg:py-section"
	id="advantages-section"
	data-animate
>
	<!-- Subtle Background Pattern -->
	<div
		class="absolute inset-0 opacity-[0.03]"
		style="background-image: url('data:image/svg+xml,%3Csvg width=\'60\' height=\'60\' viewBox=\'0 0 60 60\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cg fill=\'none\' fill-rule=\'evenodd\'%3E%3Cg fill=\'%232c2c2c\'%3E%3Cpath d=\'M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');"
	></div>

	<div class="relative mx-auto max-w-7xl px-6">
		<div class="grid gap-16 lg:grid-cols-2 lg:gap-20">
			<!-- Left: Header -->
			<div
				class="opacity-0 transition-all duration-700"
				class:animate-fade-up={sections['advantages-section']}
			>
				<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Преимущества</span>
				<h2
					class="mt-3 text-4xl font-light text-primary lg:text-5xl"
					style="font-family: var(--font-heading);"
				>
					Почему выбирают
					<span class="text-secondary">ЗОВ</span>
				</h2>
				<p class="mt-6 max-w-md text-base leading-relaxed text-text-secondary">
					Мы объединяем многолетний опыт, передовые технологии и внимание к деталям для создания
					мебели, которая превосходит ожидания.
				</p>

				<!-- Stats -->
				<div class="mt-12 grid grid-cols-2 gap-8">
					{#each stats as stat, i}
						<div
							class="opacity-0"
							class:animate-fade-up={sections['advantages-section']}
							style="animation-delay: {0.3 + i * 0.1}s"
						>
							<div
								class="text-3xl font-light text-secondary lg:text-4xl"
								style="font-family: var(--font-heading);"
							>
								{stat.value}
							</div>
							<div class="mt-1 text-sm text-text-muted">{stat.label}</div>
						</div>
					{/each}
				</div>
			</div>

			<!-- Right: Advantages List -->
			<div class="flex flex-col gap-0">
				{#each advantages as adv, i}
					<div
						class="group flex gap-6 border-b border-border-light py-8 opacity-0 transition-colors duration-300 first:border-t hover:bg-surface-warm/50 lg:px-6"
						class:animate-slide-right={sections['advantages-section']}
						style="animation-delay: {0.2 + i * 0.15}s"
					>
						<span class="mt-0.5 text-xs font-medium text-accent">{adv.number}</span>
						<div>
							<h3
								class="text-lg font-medium text-primary transition-colors duration-300 group-hover:text-secondary"
							>
								{adv.title}
							</h3>
							<p class="mt-2 text-sm leading-relaxed text-text-secondary">
								{adv.description}
							</p>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</div>
</section>

<!-- ==================== FEATURED IMAGE SECTION ==================== -->
<!-- This section overlaps with the next section -->
<section class="relative z-10 px-6" id="featured-section" data-animate>
	<div class="mx-auto max-w-7xl">
		<div
			class="relative overflow-hidden opacity-0"
			class:animate-scale-in={sections['featured-section']}
		>
			<img
				src="/images/showroom.png"
				alt="Салон мебели ЗОВ"
				class="h-[400px] w-full object-cover lg:h-[550px]"
			/>
			<div
				class="absolute inset-0 bg-gradient-to-t from-primary/80 via-primary/20 to-transparent"
			></div>

			<!-- Overlay Content -->
			<div class="absolute inset-0 flex items-end p-8 lg:p-14">
				<div class="max-w-xl">
					<h2
						class="text-3xl font-light text-white lg:text-5xl"
						style="font-family: var(--font-heading);"
					>
						Посетите наши салоны
					</h2>
					<p class="mt-4 text-sm leading-relaxed text-white/75 lg:text-base">
						Более 120 салонов по всей стране. Оцените качество материалов, прикоснитесь к текстурам
						и получите бесплатную консультацию дизайнера.
					</p>
					<a
						href="/showrooms"
						class="group mt-6 inline-flex items-center gap-3 border border-white/30 bg-white/10 px-8 py-3.5 text-xs tracking-[0.15em] text-white uppercase backdrop-blur-sm transition-all duration-500 hover:bg-white hover:text-primary"
					>
						Найти ближайший салон
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
					</a>
				</div>
			</div>
		</div>
	</div>
</section>

<!-- ==================== HARDWARE & FACADES SECTION ==================== -->
<!-- Overlapping with previous section -->
<section
	class="relative -mt-12 bg-surface-warm pt-28 pb-section-sm lg:-mt-20 lg:pt-40 lg:pb-section"
	id="details-section"
	data-animate
>
	<div class="mx-auto max-w-7xl px-6">
		<div class="grid items-center gap-12 lg:grid-cols-2 lg:gap-20">
			<!-- Image -->
			<div
				class="relative opacity-0"
				class:animate-fade-up={sections['details-section']}
				style="animation-delay: 0.2s"
			>
				<div class="relative overflow-hidden">
					<img
						src="/images/hardware.png"
						alt="Премиальная фурнитура ЗОВ"
						class="h-[400px] w-full object-cover lg:h-[500px]"
					/>
				</div>
				<!-- Floating Accent -->
				<div
					class="absolute -right-4 -bottom-4 h-24 w-24 border border-accent/30 lg:-right-6 lg:-bottom-6 lg:h-32 lg:w-32"
				></div>
			</div>

			<!-- Content -->
			<div
				class="opacity-0"
				class:animate-fade-up={sections['details-section']}
				style="animation-delay: 0.4s"
			>
				<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Детали</span>
				<h2
					class="mt-3 text-4xl font-light text-primary lg:text-5xl"
					style="font-family: var(--font-heading);"
				>
					Внимание к каждой
					<span class="text-secondary">детали</span>
				</h2>
				<p class="mt-6 text-base leading-relaxed text-text-secondary">
					Мы используем фурнитуру ведущих мировых производителей: Blum, Hettich, Grass. Каждый
					механизм работает безупречно тысячи циклов, обеспечивая плавность хода и надёжность на
					долгие годы.
				</p>
				<ul class="mt-8 flex flex-col gap-4">
					{#each ['Фасады из массива, МДФ, пластика и эмали', 'Петли с плавным закрыванием с доводчиком', 'Выкатные ящики с полным выдвижением', 'Столешницы из камня, кварца и HPL'] as item}
						<li class="flex items-start gap-3 text-sm text-text-primary">
							<svg
								class="mt-0.5 h-4 w-4 flex-shrink-0 text-accent"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								stroke-width="2"
							>
								<path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
							</svg>
							{item}
						</li>
					{/each}
				</ul>
				<div class="mt-10 flex flex-wrap gap-4">
					<a
						href="/facades"
						class="inline-flex items-center gap-2 border border-primary bg-primary px-7 py-3.5 text-xs tracking-[0.15em] text-text-inverse uppercase transition-all duration-500 hover:border-secondary hover:bg-secondary"
					>
						Фасады
					</a>
					<a
						href="/furniture"
						class="inline-flex items-center gap-2 border border-border-medium px-7 py-3.5 text-xs tracking-[0.15em] text-primary uppercase transition-all duration-500 hover:border-secondary hover:text-secondary"
					>
						Фурнитура
					</a>
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
	<!-- Decorative Elements -->
	<div class="absolute top-0 left-0 h-32 w-32 border border-white/5 lg:h-64 lg:w-64"></div>
	<div class="absolute right-0 bottom-0 h-48 w-48 border border-white/5 lg:h-80 lg:w-80"></div>

	<div class="relative mx-auto max-w-3xl px-6 text-center">
		<div class="opacity-0" class:animate-fade-up={sections['cta-section']}>
			<span class="text-[11px] tracking-[0.3em] text-accent uppercase">Начните сейчас</span>
			<h2
				class="mt-4 text-4xl font-light text-white lg:text-6xl"
				style="font-family: var(--font-heading);"
			>
				Создадим кухню
				<span class="text-accent-light">вашей мечты</span>
			</h2>
			<p class="mx-auto mt-6 max-w-lg text-base leading-relaxed text-white/60">
				Запишитесь на бесплатную консультацию в один из наших салонов. Наш дизайнер поможет
				подобрать идеальное решение для вашего пространства.
			</p>
			<div class="mt-10 flex flex-wrap items-center justify-center gap-4">
				<a
					href="/showrooms"
					class="group inline-flex items-center gap-3 border border-accent bg-accent px-8 py-4 text-xs tracking-[0.15em] text-primary uppercase transition-all duration-500 hover:border-accent-light hover:bg-accent-light"
				>
					Записаться на консультацию
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
				</a>
				<a
					href="tel:+375291234567"
					class="inline-flex items-center gap-2 border border-white/20 px-8 py-4 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:border-white/50"
				>
					<svg
						class="h-4 w-4"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
						stroke-width="1.5"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"
						/>
					</svg>
					Позвонить
				</a>
			</div>
		</div>
	</div>
</section>

<!-- Modals -->
<Modal bind:showModal={isDesignerModalOpen} title="Вызов дизайнера">
	<DesignerForm onSuccess={() => (isDesignerModalOpen = false)} />
</Modal>
