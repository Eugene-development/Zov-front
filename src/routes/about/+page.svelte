<script>
	import { onMount } from 'svelte';

	let heroVisible = $state(false);
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
			{ threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
		);

		document.querySelectorAll('[data-animate]').forEach((el) => {
			observer.observe(el);
		});

		return () => observer.disconnect();
	});

	const stats = [
		{ value: '3 000+', label: 'выполненных проектов ежегодно' },
		{ value: '2 000+', label: 'цветов и оттенков фасадов' },
		{ value: '120+', label: 'салонов по всей стране' },
		{ value: '30', label: 'лет на мебельном рынке' }
	];

	const principles = [
		{
			title: 'Открытость',
			text: 'Салоны наших дилеров работают ежедневно и всегда рады дать полную консультацию по всем вопросам'
		},
		{
			title: 'Лояльность',
			text: 'Мы всегда идём навстречу нашим клиентам в любой ситуации и дорожим долгим сотрудничеством'
		},
		{
			title: 'Поддержка',
			text: 'В сложной ситуации, при доставке или в процессе сборки, специалисты решают все вопросы в кратчайшие сроки'
		},
		{
			title: 'Качество',
			text: 'Система контроля качества и надёжная упаковка гарантирует целостность заказа и соответствие заявленному качеству'
		},
		{
			title: 'Гибкость',
			text: 'У нас гибкая политика в отношении цен, условий доставки и дат установки заказанной мебели для вашего комфорта'
		},
		{
			title: 'Инновации',
			text: 'Наша фабрика внедряет современные решения и передовые технологии в производство мебели'
		}
	];
</script>

<svelte:head>
	<title>О компании — ЗОВ | От нашей фабрики для вашей семьи</title>
	<meta
		name="description"
		content="Фабрика ЗОВ — крупнейшая сеть мебельных салонов. Более 30 лет создаём кухни и мебель премиального качества для вашей семьи."
	/>
</svelte:head>

<!-- ==================== HERO SECTION ==================== -->
<section class="relative min-h-screen overflow-hidden bg-surface" id="about-hero">
	<!-- Background Image -->
	<div class="absolute inset-0">
		<img
			src="/images/showroom.png"
			alt="Салон мебели ЗОВ"
			class="h-full w-full object-cover transition-transform duration-[2s]"
			class:scale-105={heroVisible}
		/>
		<div class="absolute inset-0 bg-gradient-to-r from-white via-white/80 to-white/30"></div>
		<div class="absolute inset-0 bg-gradient-to-t from-white/60 to-transparent"></div>
	</div>

	<!-- Content -->
	<div class="relative z-10 flex min-h-screen items-center pb-24">
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
						О фабрике
					</span>
				</div>

				<!-- Heading -->
				<h1
					class="text-5xl leading-[1.1] font-light text-primary opacity-0 md:text-6xl lg:text-7xl"
					style="font-family: var(--font-heading); animation-delay: 0.5s"
					class:animate-fade-up={heroVisible}
				>
					От нашей фабрики
					<br />
					<span class="font-normal text-secondary">для вашей семьи</span>
				</h1>

				<!-- Description -->
				<p
					class="mt-8 max-w-lg text-base leading-relaxed text-text-secondary opacity-0 md:text-lg"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.7s"
				>
					Наша фабрика располагает самой крупной сетью мебельных салонов в России и республике
					Беларусь. Предлагаем вам отличный сервис и доступные цены на мебель премиального качества.
				</p>

				<!-- CTA Buttons -->
				<div
					class="mt-10 flex flex-wrap items-center gap-4 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.9s"
				>
					<a
						href="/showrooms"
						class="group inline-flex items-center gap-3 border border-primary bg-primary px-8 py-4 text-xs tracking-[0.15em] text-text-inverse uppercase transition-all duration-500 hover:border-secondary hover:bg-secondary"
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
					<a
						href="tel:+375291234567"
						class="group inline-flex items-center gap-3 border border-border-medium bg-white/60 px-8 py-4 text-xs tracking-[0.15em] text-primary uppercase backdrop-blur-sm transition-all duration-500 hover:border-secondary hover:text-secondary"
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

<!-- ==================== MISSION + STATS SECTION ==================== -->
<section
	class="relative overflow-hidden py-section-sm lg:py-section"
	id="mission-section"
	data-animate
>
	<!-- Subtle Background Pattern -->
	<div
		class="absolute inset-0 opacity-[0.03]"
		style="background-image: url('data:image/svg+xml,%3Csvg width=\'60\' height=\'60\' viewBox=\'0 0 60 60\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cg fill=\'none\' fill-rule=\'evenodd\'%3E%3Cg fill=\'%232c2c2c\'%3E%3Cpath d=\'M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');"
	></div>

	<div class="relative mx-auto max-w-7xl px-6">
		<div class="grid gap-16 lg:grid-cols-2 lg:gap-20">
			<!-- Left: Mission -->
			<div
				class="opacity-0 transition-all duration-700"
				class:animate-fade-up={sections['mission-section']}
			>
				<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Наша миссия</span>
				<h2
					class="mt-3 text-4xl font-light text-primary lg:text-5xl"
					style="font-family: var(--font-heading);"
				>
					Мы создаём мебель,
					<span class="text-secondary">которая дарит радость</span>
				</h2>
				<div class="mt-8 space-y-5">
					<p class="text-base leading-relaxed text-text-secondary">
						Миссия нашей компании заключается в том, чтобы предоставлять клиентам высококачественную
						мебель, которая не только удовлетворяет функциональные потребности, но и приносит
						радость и комфорт в их жизни.
					</p>
					<p class="text-base leading-relaxed text-text-secondary">
						Мы уделяем особое внимание каждой детали — от выбора материалов до конечного
						производства. Тщательно подбираем только самые лучшие материалы: натуральное дерево,
						металл и стекло, — чтобы наша мебель была долговечной и выглядела прекрасно на
						протяжении многих лет.
					</p>
					<p class="text-base leading-relaxed text-text-secondary">
						Кухня и гардероб — это не просто функциональные помещения, а места, где люди проводят
						много времени. Мы учитываем потребности каждого клиента, чтобы создать мебель, которая
						идеально подходит его индивидуальному стилю.
					</p>
				</div>
			</div>

			<!-- Right: Stats -->
			<div class="flex flex-col justify-center">
				{#each stats as stat, i}
					<div
						class="group flex gap-6 border-b border-border-light py-8 opacity-0 transition-colors duration-300 first:border-t hover:bg-surface-warm/50 lg:px-6"
						class:animate-slide-right={sections['mission-section']}
						style="animation-delay: {0.2 + i * 0.15}s"
					>
						<div>
							<div
								class="text-4xl font-light text-primary transition-colors duration-300 group-hover:text-secondary lg:text-5xl"
								style="font-family: var(--font-heading);"
							>
								{stat.value}
							</div>
							<div class="mt-1 text-sm text-text-muted">{stat.label}</div>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</div>
</section>

<!-- ==================== VIDEO SECTION ==================== -->
<section class="relative z-10 px-6" id="video-section" data-animate>
	<div class="mx-auto max-w-7xl">
		<div
			class="relative overflow-hidden opacity-0"
			class:animate-scale-in={sections['video-section']}
		>
			<video
				class="h-[400px] w-full bg-black object-cover lg:h-[600px]"
				controls
				preload="metadata"
			>
				<source src="https://storage.yandexcloud.net/zovrus/zov.mp4#t=3" type="video/mp4" />
			</video>
			<!-- Video overlay gradient (hides before play) -->
			<div
				class="pointer-events-none absolute inset-0 bg-gradient-to-t from-primary/30 via-transparent to-primary/10"
			></div>
		</div>
	</div>
</section>

<!-- ==================== PRINCIPLES SECTION ==================== -->
<section
	class="relative -mt-12 bg-surface-warm pt-28 pb-section-sm lg:-mt-20 lg:pt-40 lg:pb-section"
	id="principles-section"
	data-animate
>
	<div class="mx-auto max-w-7xl px-6">
		<!-- Header -->
		<div class="mb-12 flex flex-col items-start justify-between gap-6 md:flex-row md:items-end">
			<div
				class="opacity-0 transition-all duration-700"
				class:animate-fade-up={sections['principles-section']}
			>
				<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Наши ценности</span>
				<h2
					class="mt-3 text-4xl font-light text-primary lg:text-5xl"
					style="font-family: var(--font-heading);"
				>
					Принципы компании
				</h2>
				<p class="mt-4 max-w-xl text-base leading-relaxed text-text-secondary">
					Компания основывается на принципах индивидуального подхода, высокого качества материалов и
					соблюдения сроков.
				</p>
			</div>
		</div>

		<!-- Principles Grid -->
		<div class="grid gap-6 md:grid-cols-3">
			{#each principles as principle, i}
				<div
					class="group border border-border-light bg-white p-8 shadow-card transition-all duration-500 hover:-translate-y-1 hover:shadow-elevated lg:p-10"
					class:animate-fade-up={sections['principles-section']}
					style="animation-delay: {0.2 + i * 0.1}s; opacity: 0;"
				>
					<!-- Number -->
					<span class="text-xs font-medium text-accent">0{i + 1}</span>
					<h3
						class="mt-4 text-xl font-medium text-primary transition-colors duration-300 group-hover:text-secondary lg:text-2xl"
						style="font-family: var(--font-heading);"
					>
						{principle.title}
					</h3>
					<p class="mt-3 text-sm leading-relaxed text-text-secondary">
						{principle.text}
					</p>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ==================== GALLERY / FEATURED IMAGE ==================== -->
<section class="relative z-10 px-6" id="gallery-section" data-animate>
	<div class="mx-auto max-w-7xl">
		<div
			class="relative overflow-hidden opacity-0"
			class:animate-scale-in={sections['gallery-section']}
		>
			<img
				src="/images/hero-kitchen.png"
				alt="Кухня ЗОВ в интерьере"
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
						Ждём вас в наших салонах
					</h2>
					<p class="mt-4 text-sm leading-relaxed text-white/75 lg:text-base">
						Посетите ли вы наши салоны или проконсультируетесь онлайн — в любом случае вы получите
						полную и исчерпывающую информацию о нашей мебели, фасадах, фурнитуре и о дополнительных
						услугах.
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

<!-- ==================== CTA SECTION ==================== -->
<section
	class="relative overflow-hidden bg-primary py-section-sm lg:py-section"
	id="about-cta"
	data-animate
>
	<!-- Decorative Elements -->
	<div class="absolute top-0 left-0 h-32 w-32 border border-white/5 lg:h-64 lg:w-64"></div>
	<div class="absolute right-0 bottom-0 h-48 w-48 border border-white/5 lg:h-80 lg:w-80"></div>

	<div class="relative mx-auto max-w-3xl px-6 text-center">
		<div class="opacity-0" class:animate-fade-up={sections['about-cta']}>
			<span class="text-[11px] tracking-[0.3em] text-accent uppercase">Бесплатная услуга</span>
			<h2
				class="mt-4 text-4xl font-light text-white lg:text-6xl"
				style="font-family: var(--font-heading);"
			>
				Закажите
				<span class="text-accent-light">дизайн-проект</span>
			</h2>
			<p class="mx-auto mt-6 max-w-lg text-base leading-relaxed text-white/60">
				Запишитесь на бесплатную консультацию. Наш дизайнер поможет подобрать идеальное решение для
				вашего пространства.
			</p>
			<div class="mt-10 flex flex-wrap items-center justify-center gap-4">
				<a
					href="/showrooms"
					class="group inline-flex items-center gap-3 border border-accent bg-accent px-8 py-4 text-xs tracking-[0.15em] text-primary uppercase transition-all duration-500 hover:border-accent-light hover:bg-accent-light"
				>
					Заказать дизайн-проект
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
