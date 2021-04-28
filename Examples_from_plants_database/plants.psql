--
-- PostgreSQL database dump
--

-- Dumped from database version 11.3
-- Dumped by pg_dump version 11.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: plants; Type: TABLE; Schema: public; Owner: student/postgres
--
DROP TABLE IF EXISTS public.plants CASCADE;
CREATE TABLE public.plants (
    id integer NOT NULL,
    name text,
    scientific_name text,
    is_poisonous boolean,
    primary_color text
);

ALTER TABLE public.plants OWNER TO student;

--
-- Name: plants_id_seq; Type: SEQUENCE; Schema: public; Owner: student/postgres
--
DROP SEQUENCE IF EXISTS public.plants_id_seq CASCADE;

CREATE SEQUENCE public.plants_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;



ALTER TABLE public.plants_id_seq OWNER TO student;

--
-- Name: plants_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: student/postgres
--

ALTER SEQUENCE public.plants_id_seq OWNED BY public.plants.id;


--
-- Name: plants id; Type: DEFAULT; Schema: public; Owner: student/postgres
--

ALTER TABLE ONLY public.plants ALTER COLUMN id SET DEFAULT nextval('public.plants_id_seq'::regclass);


--
-- Data for Name: plants; Type: TABLE DATA; Schema: public; Owner: student/postgres
--


COPY public.plants (id, name, scientific_name, is_poisonous, primary_color) FROM stdin;
1	Hydrangea	Hydrangea macrophylla	t	blue
2	Oleander	Nerium oleander	t	pinik
3	Water Hemlock	Cicuta	t	white
4	Bamboo	Bamboosa aridinarifolia	f	green
5	Carrot	Daucas carota	f	orange
6	Lemon	Citrus limonium	f	yellow
7	Foxglove	Digitalis	t	purple
8	Lily of the Valley	Convallaria majalis	t	white
9	Dieffenbachia	Dieffenbachia seguine	t	green
10	Tomato	Lycopersican esculentum	f	red
11	Spinach	Lactuca sativa	f	green
12	Orange	Citrus aurantium	f	orange
\.



--
-- Name: plants_id_seq; Type: SEQUENCE SET; Schema: public; Owner: student
--

SELECT pg_catalog.setval('public.plants_id_seq', 12, true);


--
-- Name: plants plants_pkey; Type: CONSTRAINT; Schema: public; Owner: student
--

ALTER TABLE ONLY public.plants
    ADD CONSTRAINT plants_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

