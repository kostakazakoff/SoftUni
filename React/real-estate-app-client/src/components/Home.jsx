import Carousel from 'react-bootstrap/Carousel';
import { useEffect, useState } from 'react';
import { fetchServer as fetchServer } from '../api/FetchServer';
import CarouselImage from './CarouselImage';

export default function Home() {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    fetchServer('list-categories')
      .then(data => setCategories(data));
  }, []);

  return (
    <Carousel style={{ textAlign: 'center' }}>
      {categories.map(category => (
        <Carousel.Item key={category.id}>
            <CarouselImage text="Rent" />
            <Carousel.Caption>
                <h3>{category.name}</h3>
            </Carousel.Caption>
        </Carousel.Item >
      ))}
    </Carousel>
  );
}