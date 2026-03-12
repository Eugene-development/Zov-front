<script lang="ts">
	import { fade } from 'svelte/transition';
	import Modal from '$lib/components/Modal.svelte';
	import ShowroomForm from '$lib/components/ShowroomForm.svelte';

	let isShowroomModalOpen = $state(false);

	// Data for styles
	const styles = [
		{
			id: 'modern',
			name: 'Современный',
			description:
				'Чистые линии, минимализм, интегрированная техника и матовые текстуры для создания идеального пространства.',
			image: '/images/style-modern.png',
			tags: ['Минимализм', 'Hi-Tech', 'Матовость']
		},
		{
			id: 'classic',
			name: 'Классика',
			description:
				'Традиционные формы, резные фасады, обилие дерева и теплые оттенки для уюта и респектабельности.',
			image: '/images/style-classic.png',
			tags: ['Дерево', 'Резьба', 'Патина']
		},
		{
			id: 'loft',
			name: 'Лофт',
			description:
				'Индустриальный шик: бетон, кирпич, металл и брутальные формы, создающие стильное современное пространство.',
			image: '/images/style-loft.png',
			tags: ['Бетон', 'Металл', 'Брутальность']
		},
		{
			id: 'neoclassic',
			name: 'Неоклассика',
			description:
				'Изящное сочетание традиционных элементов с современными материалами и светлыми тонами.',
			image: '/images/style-neoclassic.png',
			tags: ['Изящность', 'Мрамор', 'Светлые тона']
		},
		{
			id: 'minimalist',
			name: 'Скандинавский',
			description:
				'Максимум света и пространства, натуральные материалы, светлое дерево и функциональный лаконичный дизайн.',
			image: '/images/style-minimalist.png',
			tags: ['Свет', 'Уют', 'Функциональность']
		},
		{
			id: 'provence',
			name: 'Прованс',
			description:
				'Французский кантри с пастельными тонами, винтажной фурнитурой и домашним теплом.',
			image: '/images/style-provence.png',
			tags: ['Кантри', 'Винтаж', 'Уют']
		}
	];
</script>

<svelte:head>
	<title>Стили кухонь | ZOV</title>
	<meta
		name="description"
		content="Выберите идеальный стиль для вашей новой кухни ZOV. От современной минималистики до элегантной классики."
	/>
</svelte:head>

<div class="min-h-screen bg-surface text-primary selection:bg-accent-light selection:text-primary">
	<!-- Editorial Hero Section -->
	<section
		class="relative flex min-h-[90vh] flex-col items-center justify-center overflow-hidden border-b border-border-light px-4 py-20 text-center sm:px-6 lg:px-8"
	>
		<!-- Background Image -->
		<div
			class="absolute inset-0 bg-[url('/images/style-neoclassic.png')] bg-cover bg-fixed bg-center"
		></div>

		<!-- Light Overlay for readability -->
		<div class="absolute inset-0 bg-surface-warm/90 backdrop-blur-[2px]"></div>
		<div class="relative z-10 mx-auto max-w-4xl" in:fade={{ duration: 1000, delay: 200 }}>
			<span class="mb-4 block text-sm font-medium tracking-[0.2em] text-secondary uppercase">
				Коллекции
			</span>
			<h1 class="mb-8 font-heading text-6xl text-primary md:text-8xl">
				Стили <span class="text-accent italic">кухонь</span>
			</h1>
			<p
				class="mx-auto mt-8 max-w-2xl text-lg leading-relaxed font-light text-text-secondary md:text-xl"
			>
				Откройте для себя наше портфолио. <br />От строгой классики до минимализма — найдите идеальное
				решение, отражающее ваш индивидуальный вкус.
			</p>

			<div class="mt-12">
				<a
					href="#styles-grid"
					class="group inline-flex items-center justify-center gap-3 border border-border-medium bg-transparent px-8 py-4 text-xs tracking-[0.15em] text-primary uppercase transition-all duration-300 hover:border-secondary hover:text-secondary"
				>
					Выбрать стиль
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-4 w-4 transition-transform duration-300 group-hover:translate-y-1"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="1.5"
							d="M19 14l-7 7m0 0l-7-7m7 7V3"
						/>
					</svg>
				</a>
			</div>
		</div>

		<!-- Scroll Indicator -->
		<div
			class="absolute bottom-10 left-1/2 -translate-x-1/2"
			in:fade={{ duration: 1000, delay: 1000 }}
		>
			<div class="flex flex-col items-center gap-2">
				<span class="text-[10px] tracking-[0.3em] text-text-muted uppercase">Вниз</span>
				<div class="h-10 w-px bg-gradient-to-b from-border-medium to-transparent"></div>
			</div>
		</div>
	</section>

	<!-- Light Editorial Grid -->
	<section
		id="styles-grid"
		class="mx-auto max-w-7xl scroll-mt-24 px-4 py-20 sm:px-6 lg:scroll-mt-32 lg:px-8"
	>
		<div class="grid grid-cols-1 gap-12 md:grid-cols-2 lg:grid-cols-3 lg:gap-16">
			{#each styles as style}
				<div class="group flex cursor-pointer flex-col">
					<!-- Image container -->
					<div
						class="relative mb-6 aspect-[4/3] overflow-hidden bg-surface-muted transition-shadow duration-500 group-hover:shadow-medium"
					>
						<img
							src={style.image}
							alt={style.name}
							class="h-full w-full object-cover transition-transform duration-700 ease-out group-hover:scale-105"
						/>
						<!-- Subtle Hover Overlay -->
						<div
							class="absolute inset-0 bg-black/5 opacity-0 transition-opacity duration-500 group-hover:opacity-100"
						></div>
					</div>

					<!-- Content -->
					<div class="flex flex-grow flex-col text-center">
						<h2
							class="mb-3 font-heading text-3xl text-primary transition-colors group-hover:text-secondary"
						>
							{style.name}
						</h2>
						<p class="mb-6 line-clamp-3 text-sm leading-relaxed text-text-secondary">
							{style.description}
						</p>

						<div class="mt-auto flex flex-wrap justify-center gap-2">
							{#each style.tags as tag}
								<span
									class="border border-border-light bg-transparent px-3 py-1 text-xs text-text-muted transition-colors group-hover:border-secondary-light group-hover:text-secondary"
								>
									{tag}
								</span>
							{/each}
						</div>
					</div>
				</div>
			{/each}
		</div>
	</section>

	<!-- Refined Light CTA -->
	<section class="border-t border-border-light bg-white py-24">
		<div class="mx-auto max-w-4xl px-4 text-center">
			<h2 class="mb-6 font-heading text-4xl text-primary md:text-5xl">Поможем с выбором</h2>
			<p class="mx-auto mb-10 max-w-2xl text-lg font-light text-text-secondary">
				Запишитесь на встречу с нашим дизайнером. Мы подберем идеальный стиль, материалы и
				фурнитуру, учитывая архитектуру вашего пространства.
			</p>

			<button
				onclick={() => {
					isShowroomModalOpen = true;
				}}
				class="group relative inline-flex items-center justify-center gap-3 overflow-hidden border border-primary bg-primary px-8 py-4 text-sm tracking-wider text-white uppercase transition-all hover:bg-white hover:text-primary active:scale-95"
			>
				<span>Записаться в салон</span>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					class="h-4 w-4 transition-transform group-hover:translate-x-1"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M14 5l7 7m0 0l-7 7m7-7H3"
					/>
				</svg>
			</button>
		</div>
	</section>

	<!-- Modals -->
	<Modal bind:showModal={isShowroomModalOpen} title="Запись в салон">
		<ShowroomForm onSuccess={() => (isShowroomModalOpen = false)} />
	</Modal>
</div>
